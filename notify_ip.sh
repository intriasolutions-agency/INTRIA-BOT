#!/bin/bash
# Intria Bot - IP Notification Protocol
# Sends the current Public IP to Santiago on boot.

# Telegram Config
TOKEN="8046235253:AAEh37eLLtM_G3u_N5kjCskA8RAEoOjTcH8"
CHAT_ID="5122466518"

# Get IP
IP=$(curl -s http://checkip.amazonaws.com)
HOSTNAME=$(hostname)

if [ -z "$IP" ]; then
  IP="Unknown (Network Error)"
fi

MSG="🚀 *SYSTEM REBOOT DETECTED*%0A%0A*Host:* $HOSTNAME%0A*Public IP:* \`$IP\`%0A*Status:* Online & Ready."

# Send
curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d chat_id="$CHAT_ID" \
     -d text="$MSG" \
     -d parse_mode="Markdown" > /dev/null
