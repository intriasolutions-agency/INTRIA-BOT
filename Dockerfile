FROM node:22-bookworm-slim

# 1. Optimize Node memory for Free Tier
ENV NODE_OPTIONS="--max-old-space-size=512"
ENV NPM_CONFIG_LOGLEVEL=error

# 2. Install Git (Required for cloning Soul)
RUN apt-get update && \
    apt-get install -y git ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 3. Install OpenClaw (Lightweight mode)
RUN npm install -g openclaw@latest --no-audit --no-fund

# 4. Setup Workspace
WORKDIR /root/.openclaw/workspace

# 5. Prepare Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
