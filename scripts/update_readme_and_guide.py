"""
update_readme_and_guide.py
Updates README.md catalog to all 95 current problems + documents the auto-detector,
updates TRAVEL_GUIDE.md for Week 2 (Days 1-7),
and recreates LeetCode-Solutions-Java.zip.
"""

import os
import re
import zipfile

ROOT = r"E:\LeetCode-Solutions-Java"

def parse_metadata(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Extract Problem ID & Title
    prob_m = re.search(r"Problem:\s*(\d+)\.\s*([^\n\r]+)", content)
    if prob_m:
        pid = int(prob_m.group(1))
        title = prob_m.group(2).strip()
    else:
        fn = os.path.basename(filepath)
        m = re.search(r"LC(\d+)_([A-Za-z0-9]+)\.java", fn)
        pid = int(m.group(1)) if m else 0
        title = m.group(2) if m else fn

    # Extract Difficulty
    diff_m = re.search(r"Difficulty:\s*([^\n\r]+)", content)
    diff = diff_m.group(1).strip() if diff_m else "Medium"
    if "Easy" in diff:
        diff_badge = "🟢 Easy"
    elif "Hard" in diff:
        diff_badge = "🔴 Hard"
    else:
        diff_badge = "🟡 Medium"

    # Extract Category
    cat_m = re.search(r"Category:\s*([^\n\r]+)", content)
    cat = cat_m.group(1).strip() if cat_m else "Algorithms"

    # Extract Time & Space
    time_m = re.search(r"Time Complexity:\s*([^\n\r]+)", content)
    time_c = time_m.group(1).strip() if time_m else "O(N)"
    time_c = time_c.replace("O(", "$O(").replace(")", ")$") if not time_c.startswith("$") else time_c

    space_m = re.search(r"Space Complexity:\s*([^\n\r]+)", content)
    space_c = space_m.group(1).strip() if space_m else "O(1)"
    space_c = space_c.replace("O(", "$O(").replace(")", ")$") if not space_c.startswith("$") else space_c

    return {
        "id": pid,
        "title": title,
        "difficulty": diff_badge,
        "category": cat,
        "time": time_c,
        "space": space_c,
        "filename": os.path.basename(filepath)
    }

def update_readme():
    print("[*] Updating README.md...")
    java_files = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.startswith("LC") and f.endswith(".java")]
    metadata_list = [parse_metadata(f) for f in java_files]
    metadata_list.sort(key=lambda x: x["id"])

    table_rows = []
    for i, item in enumerate(metadata_list, 1):
        idx_str = f"{i:02d}"
        table_rows.append(
            f"| {idx_str} | {item['id']} | {item['title']} | {item['difficulty']} | {item['category']} | {item['time']} | {item['space']} | [`{item['filename']}`](./{item['filename']}) |"
        )

    table_text = "\n".join(table_rows)

    readme_content = f"""# LeetCode Solutions in Java 🚀

A curated collection of **{len(metadata_list)} comprehensive, production-grade Java solutions** to top LeetCode algorithm and data structure problems. Each solution includes problem statement references, algorithmic breakdowns, Big-O time and space complexity analyses, and self-contained executable `main()` test cases.

---

## ⚡ Intelligent Auto-Detector & Mobile Submissions Runner

This repository includes an autonomous **Auto-Detector & Daily Submissions Engine** designed for seamless contribution streaks from Android (Termux) or any desktop environment.

### 📱 One-Command Daily Automation
```bash
./auto_submit.sh
# or: ./run_day.sh
```
- **Self-Detecting**: Scans repository history and automatically detects which problems have already been uploaded and which day is pending.
- **Sequential Commits**: Submits the 6 daily problems sequentially with formatted commit messages (`feat(leetcode): solve LCxxxx ...`).
- **Crash-Safe & Idempotent**: Resumes seamlessly if interrupted without duplicating commits.
- **Zero Configuration Needed**: Run once per day while on mobile/travel and it handles the rest!

To check current progress without submitting:
```bash
./run_day.sh status
```

---

## 📋 Problem Catalog ({len(metadata_list)} Solutions)

| # | Problem ID | Title | Difficulty | Category / Pattern | Time Complexity | Space Complexity | Solution File |
|---|---|---|---|---|---|---|---|
{table_text}

---

## 🛠 Compilation & Execution

Each Java file is completely standalone and includes its own `main` test runner.

```bash
# Compile any single solution
javac LC0001_TwoSum.java

# Run test cases
java LC0001_TwoSum
```

To compile all files at once:
```bash
javac *.java
```
"""

    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"[+] README.md updated with {len(metadata_list)} cataloged problems.")

def update_travel_guide():
    print("[*] Updating TRAVEL_GUIDE.md...")
    guide_content = """# 📱 Termux LeetCode Auto-Submissions Guide (Week 2)

This guide allows you to maintain your GitHub contribution streak effortlessly using Termux on your Android device while traveling.

With the new **Auto-Detector Engine**, you do **not** need to manually check what is uploaded or keep track of which day you are on. Just run one single command each day!

---

## ⚡ Quick Daily Routine (Zero Friction)

Every day, simply open Termux and run:

```bash
cd ~/leetcode-solutions-java
./auto_submit.sh
```

*(Alternatively: `./run_day.sh`)*

### What the Auto-Detector Does:
1. **Scans Repository**: Detects all problems currently merged and pushed to GitHub.
2. **Finds Next Batch**: Analyzes `staging/day1` through `staging/day7` and finds the next pending day.
3. **Sequential Commits**: Copies each problem into the root directory and creates individual Git commits with clean commit messages.
4. **Pushes to GitHub**: Automatically pushes your 6 contributions for the day.
5. **Prints Summary**: Displays your active streak and remaining queued problems.

---

## 🔍 Checking Status

If you ever want to see what has been submitted vs what is pending without running commits:

```bash
./run_day.sh status
```

Example Output:
```
================================================================
⚡ LeetCode Auto-Detector & Submission Engine
================================================================
[*] Total Java solutions currently active in root: 95
----------------------------------------------------------------
  [✓] Day 1: Completed (6/6 uploaded)
  [ ] Day 2: Queued (0/6 uploaded)
  [ ] Day 3: Queued (0/6 uploaded)
  [ ] Day 4: Queued (0/6 uploaded)
  [ ] Day 5: Queued (0/6 uploaded)
  [ ] Day 6: Queued (0/6 uploaded)
  [ ] Day 7: Queued (0/6 uploaded)
----------------------------------------------------------------
⚡ Next batch queued: DAY 2. Run './auto_submit.sh' to execute.
```

---

## 📅 Week 2 Catalog Breakdown (42 Brand New Java Solutions)

### 🟢 Day 1: Arrays, Two Pointers & In-Place Manipulations
- `LC0018_4Sum.java` (Medium) — Two Pointers / 4-Sum
- `LC0027_RemoveElement.java` (Easy) — Two Pointers Fast/Slow
- `LC0080_RemoveDuplicatesFromSortedArrayII.java` (Medium) — In-Place Array Filter
- `LC0088_MergeSortedArray.java` (Easy) — 3-Pointer Reverse Fill
- `LC0209_MinimumSizeSubarraySum.java` (Medium) — Sliding Window
- `LC0283_MoveZeroes.java` (Easy) — Two Pointers In-Place Swap

### 🟢 Day 2: Linked Lists & Two-Pointer Traversals
- `LC0082_RemoveDuplicatesFromSortedListII.java` (Medium) — Sentinel Dummy Head
- `LC0083_RemoveDuplicatesFromSortedList.java` (Easy) — Linked List Deduplication
- `LC0086_PartitionList.java` (Medium) — Two Sublists Partitioning
- `LC0092_ReverseLinkedListII.java` (Medium) — Subsegment Pointer Inversion
- `LC0160_IntersectionOfTwoLinkedLists.java` (Easy) — Two Pointers Cycle/Intersection
- `LC0203_RemoveLinkedListElements.java` (Easy) — Sentinel Node Deletion

### 🟢 Day 3: Strings & Parsing / Math
- `LC0006_ZigzagConversion.java` (Medium) — Directional Simulation
- `LC0012_IntegerToRoman.java` (Medium) — Greedy Value Extraction
- `LC0013_RomanToInteger.java` (Easy) — Lookahead Subtraction
- `LC0043_MultiplyStrings.java` (Medium) — Grade-School Multiplication
- `LC0058_LengthOfLastWord.java` (Easy) — Backward Traversal
- `LC0125_ValidPalindrome.java` (Easy) — Two Pointers Alpha-Numeric

### 🟢 Day 4: Binary Search & Intervals
- `LC0057_InsertInterval.java` (Medium) — 3-Stage Interval Merge
- `LC0081_SearchInRotatedSortedArrayII.java` (Medium) — Rotated Search with Duplicates
- `LC0162_FindPeakElement.java` (Medium) — Binary Search Slope Analysis
- `LC0278_FirstBadVersion.java` (Easy) — Binary Search Boundary Condition
- `LC0704_BinarySearch.java` (Easy) — Standard Closed-Range Binary Search
- `LC0875_KokoEatingBananas.java` (Medium) — Binary Search on Answer

### 🟢 Day 5: Trees & DFS/BFS
- `LC0108_ConvertSortedArrayToBST.java` (Easy) — Divide and Conquer Height-Balanced BST
- `LC0111_MinimumDepthOfBinaryTree.java` (Easy) — BFS Level-Order Shortest Path
- `LC0112_PathSum.java` (Easy) — DFS Leaf Target Path
- `LC0113_PathSumII.java` (Medium) — DFS Path Backtracking
- `LC0129_SumRootToLeafNumbers.java` (Medium) — DFS Running Radix-10 Sum
- `LC0199_BinaryTreeRightSideView.java` (Medium) — BFS Level-Order Rightmost Node

### 🟢 Day 6: Dynamic Programming & Greedy
- `LC0045_JumpGameII.java` (Medium) — Greedy BFS Boundary Intervals
- `LC0063_UniquePathsII.java` (Medium) — 1D DP with Obstacles
- `LC0134_GasStation.java` (Medium) — Greedy Circuit Deficit Tracking
- `LC0213_HouseRobberII.java` (Medium) — Circular House Robber DP
- `LC0279_PerfectSquares.java` (Medium) — Coin-Change Style DP
- `LC0338_CountingBits.java` (Easy) — Bitwise DP Transition

### 🟢 Day 7: Bit Manipulation, Backtracking & Heaps
- `LC0029_DivideTwoIntegers.java` (Medium) — Exponential Bitwise Shifts
- `LC0077_Combinations.java` (Medium) — Pruned Backtracking
- `LC0090_SubsetsII.java` (Medium) — Backtracking with Duplicate Pruning
- `LC0202_HappyNumber.java` (Easy) — Floyd's Cycle-Finding Algorithm
- `LC0242_ValidAnagram.java` (Easy) — 26-Bucket Frequency Array
- `LC0295_FindMedianFromDataStream.java` (Hard) — Balanced Dual-Heap (Min/Max Heap)

---

## 🛠 Manual Override (Optional)

If you ever want to force-run a specific day:
```bash
./run_day.sh 1    # Force Day 1
./run_day.sh 2    # Force Day 2
# ... etc.
```

Happy submitting and enjoy your travels!
"""
    with open(os.path.join(ROOT, "TRAVEL_GUIDE.md"), "w", encoding="utf-8") as f:
        f.write(guide_content)
    print("[+] TRAVEL_GUIDE.md updated.")

def package_zip():
    print("[*] Creating LeetCode-Solutions-Java.zip...")
    zip_path = os.path.join(ROOT, "LeetCode-Solutions-Java.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)

    # Files and folders to include
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(ROOT):
            # Skip .git and __pycache__
            if ".git" in root or "__pycache__" in root or "node_modules" in root:
                continue
            for file in files:
                if file.endswith(".zip") or file.endswith(".class"):
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ROOT)
                zf.write(full_path, rel_path)
    print(f"[+] Zip package created successfully: {zip_path}")

if __name__ == "__main__":
    update_readme()
    update_travel_guide()
    package_zip()
