# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

## Browser Optimization (Tiendanube & Restricted Sites)

Para evitar bloqueos de AppArmor y el "congelamiento" del sistema al usar Chromium (Snap) en entornos restringidos, utilizar siempre el modo optimizado:

- **Comando de inicio:** `chromium-browser --remote-debugging-port=18800 --user-data-dir=/tmp/session-name --headless=new --disable-gpu --no-sandbox`
- **Razón:** El modo `headless=new` y `--no-sandbox` elimina la necesidad de renderizado gráfico y puente de seguridad que causan el time-out en el servidor.
- **Persistencia:** Si se requiere mantener la sesión, apuntar `--user-data-dir` a una ruta fija en `/home/ubuntu/.openclaw/browser/`.

---

## Infrastructure

### GitHub
- **Repo:** https://github.com/intriasolutions-agency/INTRIA-BOT.git
- **Token (PAT):** `[REDACTED - Saved in git config]`
- **User:** Intria Bot <bot@intria.agency>
