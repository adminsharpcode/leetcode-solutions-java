#!/bin/bash
# =================================================================
# Day 2 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 2 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0082_RemoveDuplicatesFromSortedListII.java
echo "[*] Processing [1/6]: LC0082 Remove Duplicates from Sorted List II..."
if [ -f "./LC0082_RemoveDuplicatesFromSortedListII.java" ] && git ls-files --error-unmatch "./LC0082_RemoveDuplicatesFromSortedListII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0082_RemoveDuplicatesFromSortedListII.java"; then
    echo "    [✓] LC0082_RemoveDuplicatesFromSortedListII.java is already committed in git repository."
else
    cp "staging/day2/LC0082_RemoveDuplicatesFromSortedListII.java" "./LC0082_RemoveDuplicatesFromSortedListII.java"
    git add "LC0082_RemoveDuplicatesFromSortedListII.java"
    git commit -m "feat(leetcode): solve LC0082 Remove Duplicates from Sorted List II in Java"
    echo "    [+] Committed [1/6]: LC0082 Remove Duplicates from Sorted List II"
    sleep 2
fi

# [2/6] LC0083_RemoveDuplicatesFromSortedList.java
echo "[*] Processing [2/6]: LC0083 Remove Duplicates from Sorted List..."
if [ -f "./LC0083_RemoveDuplicatesFromSortedList.java" ] && git ls-files --error-unmatch "./LC0083_RemoveDuplicatesFromSortedList.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0083_RemoveDuplicatesFromSortedList.java"; then
    echo "    [✓] LC0083_RemoveDuplicatesFromSortedList.java is already committed in git repository."
else
    cp "staging/day2/LC0083_RemoveDuplicatesFromSortedList.java" "./LC0083_RemoveDuplicatesFromSortedList.java"
    git add "LC0083_RemoveDuplicatesFromSortedList.java"
    git commit -m "feat(leetcode): solve LC0083 Remove Duplicates from Sorted List in Java"
    echo "    [+] Committed [2/6]: LC0083 Remove Duplicates from Sorted List"
    sleep 2
fi

# [3/6] LC0086_PartitionList.java
echo "[*] Processing [3/6]: LC0086 Partition List..."
if [ -f "./LC0086_PartitionList.java" ] && git ls-files --error-unmatch "./LC0086_PartitionList.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0086_PartitionList.java"; then
    echo "    [✓] LC0086_PartitionList.java is already committed in git repository."
else
    cp "staging/day2/LC0086_PartitionList.java" "./LC0086_PartitionList.java"
    git add "LC0086_PartitionList.java"
    git commit -m "feat(leetcode): solve LC0086 Partition List in Java"
    echo "    [+] Committed [3/6]: LC0086 Partition List"
    sleep 2
fi

# [4/6] LC0092_ReverseLinkedListII.java
echo "[*] Processing [4/6]: LC0092 Reverse Linked List II..."
if [ -f "./LC0092_ReverseLinkedListII.java" ] && git ls-files --error-unmatch "./LC0092_ReverseLinkedListII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0092_ReverseLinkedListII.java"; then
    echo "    [✓] LC0092_ReverseLinkedListII.java is already committed in git repository."
else
    cp "staging/day2/LC0092_ReverseLinkedListII.java" "./LC0092_ReverseLinkedListII.java"
    git add "LC0092_ReverseLinkedListII.java"
    git commit -m "feat(leetcode): solve LC0092 Reverse Linked List II in Java"
    echo "    [+] Committed [4/6]: LC0092 Reverse Linked List II"
    sleep 2
fi

# [5/6] LC0160_IntersectionOfTwoLinkedLists.java
echo "[*] Processing [5/6]: LC0160 Intersection of Two Linked Lists..."
if [ -f "./LC0160_IntersectionOfTwoLinkedLists.java" ] && git ls-files --error-unmatch "./LC0160_IntersectionOfTwoLinkedLists.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0160_IntersectionOfTwoLinkedLists.java"; then
    echo "    [✓] LC0160_IntersectionOfTwoLinkedLists.java is already committed in git repository."
else
    cp "staging/day2/LC0160_IntersectionOfTwoLinkedLists.java" "./LC0160_IntersectionOfTwoLinkedLists.java"
    git add "LC0160_IntersectionOfTwoLinkedLists.java"
    git commit -m "feat(leetcode): solve LC0160 Intersection of Two Linked Lists in Java"
    echo "    [+] Committed [5/6]: LC0160 Intersection of Two Linked Lists"
    sleep 2
fi

# [6/6] LC0203_RemoveLinkedListElements.java
echo "[*] Processing [6/6]: LC0203 Remove Linked List Elements..."
if [ -f "./LC0203_RemoveLinkedListElements.java" ] && git ls-files --error-unmatch "./LC0203_RemoveLinkedListElements.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0203_RemoveLinkedListElements.java"; then
    echo "    [✓] LC0203_RemoveLinkedListElements.java is already committed in git repository."
else
    cp "staging/day2/LC0203_RemoveLinkedListElements.java" "./LC0203_RemoveLinkedListElements.java"
    git add "LC0203_RemoveLinkedListElements.java"
    git commit -m "feat(leetcode): solve LC0203 Remove Linked List Elements in Java"
    echo "    [+] Committed [6/6]: LC0203 Remove Linked List Elements"
    sleep 2
fi

echo "================================================================"
echo "[*] Day 2 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 2 complete! 6 contributions pushed to GitHub."
echo "================================================================"
