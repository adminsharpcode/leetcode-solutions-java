#!/bin/bash
# ===============================================================
# One-time Termux Setup Script for Android
# ===============================================================
set -e

echo "=================================================="
echo "📱 Termux Setup for LeetCode GitHub Submissions"
echo "=================================================="

echo "[*] Updating package index..."
pkg update -y

echo "[*] Installing Git & GitHub CLI..."
pkg install -y git gh

echo "[*] Configuring Git identity..."
git config --global user.name "adminsharpcode"
git config --global user.email "57152749+adminsharpcode@users.noreply.github.com"

echo "[*] Making all daily shell scripts executable..."
chmod +x day*.sh run_day.sh

echo ""
echo "=================================================="
echo "✅ Setup Complete!"
echo "=================================================="
echo "If you have not authenticated with GitHub on Termux yet, run:"
echo "   gh auth login"
echo "Select: GitHub.com -> HTTPS -> Login with a web browser"
echo ""
echo "Then each day, simply run:"
echo "   ./run_day.sh 1   (Day 1)"
echo "   ./run_day.sh 2   (Day 2)"
echo "   ..."
echo "   ./run_day.sh 7   (Day 7)"
echo "=================================================="
