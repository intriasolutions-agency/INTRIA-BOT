FROM node:22-bookworm-slim

# Install dependencies (Minimal)
RUN apt-get update && apt-get install -y \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install OpenClaw globally
RUN npm install -g openclaw@latest

# Create workspace
WORKDIR /root/.openclaw/workspace

# Copy local backup script to entrypoint (will be overwritten by git pull in real usage)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
