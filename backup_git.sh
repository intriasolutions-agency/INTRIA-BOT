#!/bin/bash
# Intria Bot - Auto Backup to GitHub
# Pushes MEMORY, AGENTS, and Configs to the repo daily.

LOGFILE="/home/ubuntu/.openclaw/workspace/backup.log"
REPO_DIR="/home/ubuntu/.openclaw/workspace"

echo "--- Starting Backup: $(date) ---" >> "$LOGFILE"

cd "$REPO_DIR" || exit

# 1. Add key files
git add MEMORY.md AGENTS.md TOOLS.md SOUL.md maintenance.sh notify_ip.sh watchdog.sh rescue-backup/

# 2. Commit
COMMIT_MSG="Auto-Backup: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MSG" >> "$LOGFILE" 2>&1

# 3. Push
git push origin master >> "$LOGFILE" 2>&1

if [ $? -eq 0 ]; then
  echo "Backup Successful." >> "$LOGFILE"
else
  echo "Backup Failed." >> "$LOGFILE"
fi
