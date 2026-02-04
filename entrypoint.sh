#!/bin/bash
# Intria Bot - Resurrection Entrypoint

echo "🔥 INTRIA PHOENIX PROTOCOL INITIATED 🔥"

# 1. Clone/Pull Soul from GitHub
REPO_URL="https://github.com/intriasolutions-agency/INTRIA-BOT.git"
if [ -d ".git" ]; then
    echo "🧠 Updating memory from GitHub..."
    git pull origin master
else
    echo "🧠 Downloading soul from GitHub..."
    git clone "$REPO_URL" .
fi

# 2. Restore Config (User must provide secrets via ENV)
if [ ! -f "/root/.openclaw/openclaw.json" ]; then
    echo "⚙️  Generating config from environment..."
    # Create a basic config using env vars
    openclaw onboard --defaults --no-interaction
fi

# 3. Start Gateway
echo "🚀 LAUNCHING INTRIA BOT..."
exec openclaw gateway run
