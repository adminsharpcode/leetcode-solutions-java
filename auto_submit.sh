#!/bin/sh
# auto_submit.sh — Week 3 auto-detector & runner
# Detects which day has pending submissions and runs it.
set -e
echo "=============================="
echo " LeetCode Auto-Submit Week 3  "
echo "=============================="
echo ""
echo "Checking submission status..."
echo ""

  # Check Day 1
  DAY1_DONE=1
  for f in staging/day1/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY1_DONE=0
      break
    fi
  done
  if [ "$DAY1_DONE" = "0" ]; then
    echo ">>> Running Day 1..."
    sh day1.sh
    echo "Day 1 complete."
    exit 0
  else
    echo "Day 1: already fully submitted."
  fi

  # Check Day 2
  DAY2_DONE=1
  for f in staging/day2/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY2_DONE=0
      break
    fi
  done
  if [ "$DAY2_DONE" = "0" ]; then
    echo ">>> Running Day 2..."
    sh day2.sh
    echo "Day 2 complete."
    exit 0
  else
    echo "Day 2: already fully submitted."
  fi

  # Check Day 3
  DAY3_DONE=1
  for f in staging/day3/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY3_DONE=0
      break
    fi
  done
  if [ "$DAY3_DONE" = "0" ]; then
    echo ">>> Running Day 3..."
    sh day3.sh
    echo "Day 3 complete."
    exit 0
  else
    echo "Day 3: already fully submitted."
  fi

  # Check Day 4
  DAY4_DONE=1
  for f in staging/day4/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY4_DONE=0
      break
    fi
  done
  if [ "$DAY4_DONE" = "0" ]; then
    echo ">>> Running Day 4..."
    sh day4.sh
    echo "Day 4 complete."
    exit 0
  else
    echo "Day 4: already fully submitted."
  fi

  # Check Day 5
  DAY5_DONE=1
  for f in staging/day5/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY5_DONE=0
      break
    fi
  done
  if [ "$DAY5_DONE" = "0" ]; then
    echo ">>> Running Day 5..."
    sh day5.sh
    echo "Day 5 complete."
    exit 0
  else
    echo "Day 5: already fully submitted."
  fi

  # Check Day 6
  DAY6_DONE=1
  for f in staging/day6/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY6_DONE=0
      break
    fi
  done
  if [ "$DAY6_DONE" = "0" ]; then
    echo ">>> Running Day 6..."
    sh day6.sh
    echo "Day 6 complete."
    exit 0
  else
    echo "Day 6: already fully submitted."
  fi

  # Check Day 7
  DAY7_DONE=1
  for f in staging/day7/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY7_DONE=0
      break
    fi
  done
  if [ "$DAY7_DONE" = "0" ]; then
    echo ">>> Running Day 7..."
    sh day7.sh
    echo "Day 7 complete."
    exit 0
  else
    echo "Day 7: already fully submitted."
  fi
echo ""
echo "DONE: All Week 3 days are fully submitted!"
