#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
setup_env.py
지식 위키(llmwiki) 및 에이전트 자산(스킬, 프로필)의 이식성 부트스트랩.

1) 레포 내 skills/ · hermes/profiles/ 를 ~/.gemini · ~/.hermes 에 심링크
2) 각 프로필 .env 에 WIKI_PATH=<이 레포 절대경로> 를 upsert (단일 정의 주체)
3) --init-env: .env 없으면 .env.template 에서 생성 (시크릿은 수동 채움)

WIKI_PATH = llmwiki 레포 루트 (wiki/ 가 아님).
  위키 본문: ${WIKI_PATH}/wiki/
  운영 일지: ${WIKI_PATH}/memory.md
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SKILLS_SRC = REPO_ROOT / "skills"
PROFILES_SRC = REPO_ROOT / "hermes" / "profiles"

WIKI_PATH_LINE_RE = re.compile(r"(?m)^(?:export\s+)?WIKI_PATH=.*$")


def get_target_dirs():
    home = Path.home()
    return home / ".gemini" / "config" / "skills", home / ".hermes" / "profiles"


def create_symlink(src: Path, dest: Path, dry_run=False, force=False) -> bool:
    if dry_run:
        print(f"[Dry-run] Link: {src} -> {dest}")
        return True

    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() or dest.is_symlink():
        if force:
            if dest.is_symlink() or dest.is_file():
                dest.unlink()
            elif dest.is_dir():
                shutil.rmtree(dest)
        else:
            print(f"[Skipped] 이미 존재함 (덮어쓰려면 --force 사용): {dest}")
            return False

    try:
        dest.symlink_to(src, target_is_directory=src.is_dir())
        print(f"[Linked] {src.name} -> {dest}")
        return True
    except OSError as e:
        print(f"[Error] 심링크 생성 실패: {dest} ({e})")
        if sys.platform.startswith("win"):
            print(
                "Windows에서는 심링크에 관리자 권한이 필요할 수 있습니다."
            )
        return False


def sync_skills(target_dir: Path, dry_run=False, force=False) -> int:
    print("\n>>> 1. 스킬(skills) 동기화")
    if not SKILLS_SRC.exists():
        print(f"[Warning] 소스 없음: {SKILLS_SRC}")
        return 0

    count = 0
    for skill_path in sorted(SKILLS_SRC.iterdir()):
        if skill_path.is_dir():
            if create_symlink(skill_path, target_dir / skill_path.name, dry_run, force):
                count += 1
    print(f"스킬 완료: {count}개 연결됨.")
    return count


def sync_profiles(target_dir: Path, dry_run=False, force=False) -> int:
    print("\n>>> 2. 프로필(profiles) 동기화")
    if not PROFILES_SRC.exists():
        print(f"[Warning] 소스 없음: {PROFILES_SRC}")
        return 0

    count = 0
    for profile_path in sorted(PROFILES_SRC.iterdir()):
        if not profile_path.is_dir():
            continue
        dest_profile_dir = target_dir / profile_path.name
        if not dry_run:
            dest_profile_dir.mkdir(parents=True, exist_ok=True)

        for file_name in [".env", "SOUL.md"]:
            src_file = profile_path / file_name
            dest_file = dest_profile_dir / file_name
            if src_file.exists():
                if create_symlink(src_file, dest_file, dry_run, force):
                    count += 1
            elif (
                file_name == ".env"
                and dry_run
                and (profile_path / ".env.template").exists()
            ):
                # --init-env dry-run: .env will exist before real link step
                if create_symlink(profile_path / ".env", dest_file, dry_run, force):
                    count += 1
    print(f"프로필 파일 완료: {count}개 파일 연결됨.")
    return count


def upsert_wiki_path(env_path: Path, wiki_path: str, dry_run=False) -> str:
    """Set WIKI_PATH=<repo root> in .env. Returns action: created|updated|unchanged|dry-run."""
    line = f"WIKI_PATH={wiki_path}"
    if not env_path.exists():
        template = env_path.parent / ".env.template"
        if dry_run and template.exists():
            print(f"[Dry-run] WIKI_PATH (after init): {env_path} -> {wiki_path}")
            return "dry-run:after-init"
        return "missing"

    text = env_path.read_text(encoding="utf-8")
    if WIKI_PATH_LINE_RE.search(text):
        new_text = WIKI_PATH_LINE_RE.sub(line, text)
        action = "unchanged" if new_text == text else "updated"
    else:
        if text and not text.endswith("\n"):
            text += "\n"
        new_text = (
            text
            + "\n# LLM knowledge wiki (Karpathy) — llmwiki repo root\n"
            + line
            + "\n"
        )
        action = "created"

    if dry_run:
        print(f"[Dry-run] WIKI_PATH ({action}): {env_path} -> {wiki_path}")
        return f"dry-run:{action}"

    if action != "unchanged":
        env_path.write_text(new_text, encoding="utf-8")
    print(f"[WIKI_PATH {action}] {env_path.parent.name}: {wiki_path}")
    return action


def init_env_files(dry_run=False) -> int:
    """Copy .env.template -> .env when .env is missing."""
    print("\n>>> 3. .env 초기화 (--init-env)")
    created = 0
    for profile in sorted(PROFILES_SRC.iterdir()):
        if not profile.is_dir():
            continue
        env = profile / ".env"
        template = profile / ".env.template"
        if env.exists():
            continue
        if not template.exists():
            print(f"[Warning] 템플릿 없음: {template}")
            continue
        if dry_run:
            print(f"[Dry-run] Copy {template.name} -> {env}")
            created += 1
            continue
        shutil.copy2(template, env)
        print(f"[Created] {env.relative_to(REPO_ROOT)} from template")
        created += 1
    print(f".env 신규 생성: {created}개")
    return created


def inject_wiki_paths(dry_run=False) -> dict:
    """Upsert WIKI_PATH into every profile .env. WIKI_PATH = REPO_ROOT (not .../wiki)."""
    print("\n>>> 4. WIKI_PATH 주입 (레포 루트)")
    wiki_path = str(REPO_ROOT)
    results = {}
    for profile in sorted(PROFILES_SRC.iterdir()):
        if not profile.is_dir():
            continue
        env = profile / ".env"
        results[profile.name] = upsert_wiki_path(env, wiki_path, dry_run=dry_run)
    return results


def main():
    parser = argparse.ArgumentParser(
        description="llmwiki 에이전트 환경 원클릭 복구 (심링크 + WIKI_PATH 주입)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="실제 변경 없이 예정 작업만 출력",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="기존 링크/파일 강제 교체",
    )
    parser.add_argument(
        "--init-env",
        action="store_true",
        help=".env 없으면 .env.template 에서 생성",
    )
    parser.add_argument(
        "--skip-links",
        action="store_true",
        help="심링크 생략 (WIKI_PATH / --init-env 만)",
    )
    args = parser.parse_args()

    gemini_skills_dir, hermes_profiles_dir = get_target_dirs()

    print(f"=== 에이전트 환경 동기화 (Platform: {sys.platform}) ===")
    print(f"REPO_ROOT = {REPO_ROOT}")
    print(f"WIKI_PATH = {REPO_ROOT}  (wiki/={REPO_ROOT / 'wiki'}, memory={REPO_ROOT / 'memory.md'})")
    if args.dry_run:
        print("※ Dry-run — 파일 변경 없음\n")

    # Order matters: create .env before linking/injecting so new machines get 22 profile files.
    if args.init_env:
        init_env_files(args.dry_run)

    wiki_results = inject_wiki_paths(args.dry_run)

    skill_count = 0
    profile_count = 0
    if not args.skip_links:
        skill_count = sync_skills(gemini_skills_dir, args.dry_run, args.force)
        profile_count = sync_profiles(hermes_profiles_dir, args.dry_run, args.force)

    injected = sum(
        1
        for v in wiki_results.values()
        if v not in ("missing",) and not str(v).endswith("missing")
    )

    print("\n=== 검증 요약 ===")
    print(f"스킬 링크: {skill_count} (기대 ≥18)")
    print(f"프로필 파일 링크: {profile_count} (기대 ≥22 = 11×(SOUL.md+.env))")
    print(f"WIKI_PATH 주입 대상: {injected}/{len(wiki_results)}")
    for name, action in wiki_results.items():
        print(f"  - {name}: {action}")

    print("\n=== 완료 ===")
    print(
        "새 기기: git clone → python3 setup_env.py --init-env --force "
        "→ 각 .env 시크릿 수동 채움"
    )


if __name__ == "__main__":
    main()
