#!/bin/bash
# Intria Bot Watchdog - The Guardian
# Checks if the Gateway is alive. If not, restarts it.

URL="http://127.0.0.1:18789/health"
SERVICE="openclaw"
LOGfile="/home/ubuntu/.openclaw/workspace/watchdog.log"

# Check status code
STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$URL")

if [ "$STATUS" != "200" ]; then
  echo "$(date): CRITICAL - Gateway unresponsive (Status: $STATUS). Reviving..." >> "$LOGfile"
  
  # Emergency Notification
  TOKEN="8046235253:AAEh37eLLtM_G3u_N5kjCskA8RAEoOjTcH8"
  CHAT_ID="5122466518"
  MSG="🚨 *SISTEMA COMPROMETIDO DETECTADO* 🚨%0A%0AEl Guardián ha detectado que Intria Bot no responde.%0AIniciando protocolo de resurrección de emergencia...%0A%0A_No se requiere acción humana._"
  curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" -d chat_id="$CHAT_ID" -d text="$MSG" -d parse_mode="Markdown" >/dev/null

  sudo systemctl restart "$SERVICE"
  echo "$(date): Restart triggered." >> "$LOGfile"
else
  # Optional: Log heartbeat only occasionally to avoid spam
  # echo "$(date): OK - Gateway is alive." >> "$LOGfile"
  :
fi
