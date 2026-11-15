"""
detector.py
Analyzes the LeetCode repository to detect which problems have been submitted,
which staging problems are pending, and optionally runs the next daily batch.
"""

import os
import sys
import subprocess
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_root_solutions():
    files = [f for f in os.listdir(ROOT) if f.startswith("LC") and f.endswith(".java")]
    return sorted(files)

def analyze_staging():
    days = {}
    for day in range(1, 8):
        day_dir = os.path.join(ROOT, "staging", f"day{day}")
        if not os.path.isdir(day_dir):
            continue
        day_files = sorted([f for f in os.listdir(day_dir) if f.startswith("LC") and f.endswith(".java")])
        days[day] = day_files
    return days

def report_status():
    root_sols = set(get_root_solutions())
    staging_days = analyze_staging()

    print("=" * 64)
    print("🔍 LEETCODE REPOSITORY UPLOAD DETECTOR")
    print("=" * 64)
    print(f"Total problems active in repository root: {len(root_sols)}")
    print("-" * 64)

    next_day = None
    all_completed = True

    for day, files in staging_days.items():
        completed = [f for f in files if f in root_sols]
        pending = [f for f in files if f not in root_sols]

        if len(pending) == 0:
            status_str = "✅ COMPLETED"
        elif len(completed) > 0:
            status_str = f"⚡ PARTIAL ({len(completed)}/{len(files)} uploaded)"
            if next_day is None:
                next_day = day
                all_completed = False
        else:
            status_str = f"⏳ QUEUED (0/{len(files)} uploaded)"
            if next_day is None:
                next_day = day
                all_completed = False

        print(f"Day {day} [{status_str}]:")
        for f in files:
            mark = "  [✓]" if f in root_sols else "  [ ]"
            print(f"  {mark} {f}")
        print()

    print("-" * 64)
    if all_completed:
        print("🎉 ALL 42 STAGING PROBLEMS ACROSS ALL 7 DAYS ARE FULLY SUBMITTED!")
    else:
        print(f"⚡ NEXT BATCH RECOMMENDED: DAY {next_day}")
    print("=" * 64)
    return next_day

def run_day(day_num):
    day_script = os.path.join(ROOT, f"day{day_num}.sh")
    if sys.platform == "win32":
        # In windows shell, execute via bash or python equivalent
        bash_path = "bash"
        cmd = [bash_path, day_script]
        print(f"[*] Executing Day {day_num} via bash...")
        subprocess.run(cmd, check=True)
    else:
        subprocess.run(["bash", day_script], check=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--run-next", "-r", "auto"):
        next_d = report_status()
        if next_d:
            print(f"\n[*] Launching Day {next_d} automatically...")
            run_day(next_d)
    else:
        report_status()
