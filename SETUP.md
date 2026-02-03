# Manual de Despliegue - INTRIA BOT 🚀

Este repositorio contiene la inteligencia y las habilidades de Intria Bot. Para desplegar en un nuevo servidor (potente), seguir estos pasos:

## 1. Requisitos del Sistema
- **SO:** Linux (Ubuntu recomendado) / macOS.
- **Node.js:** v22.x o superior.
- **Espacio en Disco:** Mínimo 20GB (para procesamiento de video/IA).
- **RAM:** Mínimo 4GB (recomendado 8GB+ para tareas pesadas).

## 2. Dependencias Externas (Instalar en el host)
```bash
# Para procesamiento de video y audio
sudo apt-get install -y ffmpeg

# Para IA de transcripción (Whisper)
pip3 install openai-whisper

# Para navegación web y capturas
sudo snap install chromium
```

## 3. Configuración de OpenClaw
1. Clonar este repositorio.
2. Instalar OpenClaw: `npm install -g openclaw`
3. Configurar el entorno con las API Keys correspondientes (Google Gemini, ElevenLabs).

## 4. Skills Disponibles
- **Gestión:** Gmail, GitHub, Notion.
- **Multimedia:** ElevenLabs TTS, Remotion (Requiere servidor potente).
- **Utilidades:** 1Password CLI.

---
*Última actualización: 2026-02-03 - Intria Bot*
