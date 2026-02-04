#!/bin/bash
# Intria Bot - Daily Maintenance & Cleanup
# Keeps the server clean to prevent "No space left on device"

LOGFILE="/home/ubuntu/.openclaw/workspace/maintenance.log"

echo "--- Starting Maintenance: $(date) ---" >> "$LOGFILE"

# 1. Clean Package Manager Cache (npm/yarn)
echo "Cleaning npm cache..." >> "$LOGFILE"
npm cache clean --force 2>/dev/null

# 2. Clean Systemd Journals (Keep only last 2 days)
echo "Cleaning systemd journals..." >> "$LOGFILE"
sudo journalctl --vacuum-time=2d 2>/dev/null

# 3. Clean Temp Files (older than 3 days)
echo "Cleaning /tmp..." >> "$LOGFILE"
find /tmp -type f -atime +3 -delete 2>/dev/null

# 4. Clean Browser Cache (Chromium/Chrome)
echo "Cleaning browser cache..." >> "$LOGFILE"
rm -rf /home/ubuntu/.cache/chromium/Default/Cache/* 2>/dev/null
rm -rf /home/ubuntu/.cache/google-chrome/Default/Cache/* 2>/dev/null

# 5. Git Maintenance (Pack objects to save space)
echo "Optimizing git repo..." >> "$LOGFILE"
git gc --auto 2>/dev/null

echo "--- Maintenance Complete: $(date) ---" >> "$LOGFILE"
