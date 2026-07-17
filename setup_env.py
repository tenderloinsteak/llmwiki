#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
setup_env.py
지식 위키(llmwiki) 및 에이전트 자산(스킬, 프로필)의 100% 이식성 확보를 위한 부트스트랩 스크립트.
레포 내 저장된 설정 파일들을 로컬 에이전트 구동 경로(~/.gemini, ~/.hermes)에 자동으로 심링크 연결해 줍니다.
"""

import os
import sys
import argparse
from pathlib import Path

# 기준 경로 설정 (스크립트 위치)
REPO_ROOT = Path(__file__).resolve().parent
SKILLS_SRC = REPO_ROOT / "skills"
PROFILES_SRC = REPO_ROOT / "hermes" / "profiles"

def get_target_dirs():
    """OS에 따른 에이전트 로컬 기본 설정 디렉토리 반환"""
    home = Path.home()
    gemini_skills_dir = home / ".gemini" / "config" / "skills"
    hermes_profiles_dir = home / ".hermes" / "profiles"
    return gemini_skills_dir, hermes_profiles_dir

def create_symlink(src: Path, dest: Path, dry_run=False, force=False):
    """안전한 심링크 생성 처리"""
    if dry_run:
        print(f"[Dry-run] Link: {src} -> {dest}")
        return True

    # 부모 디렉토리 생성
    dest.parent.mkdir(parents=True, exist_ok=True)

    # 대상이 이미 존재하는 경우
    if dest.exists() or dest.is_symlink():
        if force:
            if dest.is_symlink() or dest.is_file():
                dest.unlink()
            elif dest.is_dir():
                import shutil
                shutil.rmtree(dest)
        else:
            print(f"[Skipped] 이미 존재함 (덮어쓰려면 --force 사용): {dest}")
            return False

    try:
        # OS별 심링크 처리 (윈도우의 경우 관리자 권한 예외가 발생할 수 있음)
        dest.symlink_to(src, target_is_directory=src.is_dir())
        print(f"[Linked] {src.name} -> {dest}")
        return True
    except OSError as e:
        print(f"[Error] 심링크 생성 실패: {dest} ({e})")
        if sys.platform.startswith("win"):
            print("Windows 환경에서는 심링크 생성을 위해 관리자 권한이 필요할 수 있습니다. 터미널을 관리자 권한으로 실행해 주세요.")
        return False

def sync_skills(target_dir: Path, dry_run=False, force=False):
    """skills 동기화"""
    print("\n>>> 1. 스킬(skills) 동기화 진행 중...")
    if not SKILLS_SRC.exists():
        print(f"[Warning] 소스 스킬 디렉토리가 존재하지 않습니다: {SKILLS_SRC}")
        return

    count = 0
    for skill_path in SKILLS_SRC.iterdir():
        if skill_path.is_dir():
            dest_path = target_dir / skill_path.name
            if create_symlink(skill_path, dest_path, dry_run, force):
                count += 1
    print(f"스킬 완료: {count}개 연결됨.")

def sync_profiles(target_dir: Path, dry_run=False, force=False):
    """personas 프로필( souls ) 동기화"""
    print("\n>>> 2. 프로필(profiles) 동기화 진행 중...")
    if not PROFILES_SRC.exists():
        print(f"[Warning] 소스 프로필 디렉토리가 존재하지 않습니다: {PROFILES_SRC}")
        return

    count = 0
    for profile_path in PROFILES_SRC.iterdir():
        if profile_path.is_dir():
            # 프로필 폴더는 런타임 캐시가 섞이므로 폴더째 심링크를 걸지 않고, 내부 파일(.env, SOUL.md)만 각각 건다.
            dest_profile_dir = target_dir / profile_path.name
            dest_profile_dir.mkdir(parents=True, exist_ok=True)

            for file_name in [".env", "SOUL.md"]:
                src_file = profile_path / file_name
                if src_file.exists():
                    dest_file = dest_profile_dir / file_name
                    if create_symlink(src_file, dest_file, dry_run, force):
                        count += 1
    print(f"프로필 파일 완료: {count}개 파일 연결됨.")

def main():
    parser = argparse.ArgumentParser(description="Mantis Algo / llmwiki 에이전트 환경 원클릭 복구 및 심링크 셋업 도구")
    parser.add_argument("--dry-run", action="store_true", help="실제 변경을 가하지 않고 링크 예상 위치만 시뮬레이션 출력합니다.")
    parser.add_argument("--force", action="store_true", help="기존 링크나 파일이 존재하더라도 강제로 지우고 새로 연결합니다.")
    
    args = parser.parse_args()

    gemini_skills_dir, hermes_profiles_dir = get_target_dirs()

    print(f"=== 에이전트 환경 동기화 시작 (Platform: {sys.platform}) ===")
    if args.dry_run:
        print("※ [주의] Dry-run 모드로 실행되어 실제 파일 변경은 일어나지 않습니다.\n")

    sync_skills(gemini_skills_dir, args.dry_run, args.force)
    sync_profiles(hermes_profiles_dir, args.dry_run, args.force)
    
    print("\n=== 환경 구축 완료 ===")
    print("컴퓨터를 바꾸더라도 git clone 후 'python3 setup_env.py --force'를 한 번 실행해 주면 즉시 100% 동일한 환경이 재구성됩니다.")

if __name__ == "__main__":
    main()
