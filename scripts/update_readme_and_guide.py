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
    guide_content = """# 📱 Termux LeetCode Auto-Submissions Guide (Week 3)

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

---

## 📅 Week 3 Catalog Breakdown (42 Brand New Java Solutions)

### 🟢 Day 1: Graphs & BFS / Union Find
- `LC0127_WordLadder.java` (Hard) — Breadth-First Search / Mutating Characters
- `LC0130_SurroundedRegions.java` (Medium) — Boundary DFS In-Place Flood Fill
- `LC0261_GraphValidTree.java` (Medium) — Disjoint Set Union (DSU) Cycle Detection
- `LC0310_MinimumHeightTrees.java` (Medium) — BFS Topological Leaf Trimming
- `LC0399_EvaluateDivision.java` (Medium) — Graph DFS Path Product
- `LC0547_NumberOfProvinces.java` (Medium) — Connected Components DFS / DSU

### 🟢 Day 2: Stack & Monotonic Stack
- `LC0085_MaximalRectangle.java` (Hard) — Monotonic Stack on 2D Histogram Heights
- `LC0316_RemoveDuplicateLetters.java` (Medium) — Greedy Monotonic Stack with Frequency Tracking
- `LC0394_DecodeString.java` (Medium) — Dual Stacks (Multipliers & StringBuffers)
- `LC0496_NextGreaterElementI.java` (Easy) — Monotonic Decreasing Stack + HashMap
- `LC0503_NextGreaterElementII.java` (Medium) — Circular Monotonic Decreasing Index Stack
- `LC0739_DailyTemperatures.java` (Medium) — Monotonic Decreasing Stack Index Spans

### 🟢 Day 3: Sliding Window & Two Pointers
- `LC0030_SubstringConcatenation.java` (Hard) — Fixed-Length Sliding Window with Word Frequency Maps
- `LC0159_LongestSubstringTwoDistinct.java` (Medium) — Dynamic Sliding Window with 2 Distinct Chars
- `LC0239_SlidingWindowMaximum.java` (Hard) — Monotonic Decreasing Deque Window Bounds
- `LC0567_PermutationInString.java` (Medium) — Fixed-Length Frequency Difference Window
- `LC0632_SmallestRange.java` (Hard) — K-Pointer Min-Heap with Maximum Tracker
- `LC0643_MaximumAverageSubarrayI.java` (Easy) — Fixed-Length Sliding Window Running Sum

### 🟢 Day 4: Bit Manipulation & Math
- `LC0190_ReverseBits.java` (Easy) — 32-Bit Shift and Mask
- `LC0191_NumberOf1Bits.java` (Easy) — Brian Kernighan's Bit Manipulation
- `LC0231_PowerOfTwo.java` (Easy) — Single Set Bit Validation
- `LC0260_SingleNumberIII.java` (Medium) — Two-Bucket Bit Partitioning by Lowest Diff Bit
- `LC0268_MissingNumber.java` (Easy) — Gauss Formula / XOR Sum
- `LC0371_SumOfTwoIntegers.java` (Medium) — Bitwise Adder Simulation (XOR & Carry Shift)

### 🟢 Day 5: Dynamic Programming (2D & State Transitions)
- `LC0097_InterleavingString.java` (Medium) — 2D Matrix Interleaving DP
- `LC0115_DistinctSubsequences.java` (Hard) — 2D Subsequence Matching DP
- `LC0132_PalindromePartitioningII.java` (Hard) — Palindrome Table + 1D Min-Cut DP
- `LC0188_BestTimeToBuyAndSellStockIV.java` (Hard) — K-Transaction Buy/Sell DP
- `LC0309_BestTimeCooldown.java` (Medium) — 3-State Finite State Machine DP (Held, Sold, Rest)
- `LC0518_CoinChangeII.java` (Medium) — Unbounded Knapsack / Combinations DP

### 🟢 Day 6: Trie & String Algorithms
- `LC0211_DesignAddSearchWords.java` (Medium) — 26-Way Trie with Recursive DFS Wildcard Matching
- `LC0212_WordSearchII.java` (Hard) — 2D Grid DFS Backtracking over Prefix Trie
- `LC0336_PalindromePairs.java` (Hard) — Reversed Prefix/Suffix Palindrome Matching
- `LC0421_MaximumXOR.java` (Medium) — Bitwise Prefix Trie Greedy Bit Inversion
- `LC0472_ConcatenatedWords.java` (Hard) — Dictionary Set + 1D DP Word Formation
- `LC0648_ReplaceWords.java` (Medium) — Prefix Trie Shortest Root Substitution

### 🟢 Day 7: Advanced Trees & LCA
- `LC0297_SerializeDeserializeBinaryTree.java` (Hard) — Preorder DFS with Null Sentinels
- `LC0450_DeleteNodeInBST.java` (Medium) — BST Key Search + In-Order Successor Deletion
- `LC0538_ConvertBSTToGreaterTree.java` (Medium) — Reverse In-Order DFS Accumulator
- `LC0543_DiameterOfBinaryTree.java` (Easy) — Post-Order DFS Max Depth Span
- `LC0572_SubtreeOfAnotherTree.java` (Easy) — Subtree Equality DFS Traversal
- `LC0652_FindDuplicateSubtrees.java` (Medium) — Post-Order Serialization HashMap Deduplication

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
