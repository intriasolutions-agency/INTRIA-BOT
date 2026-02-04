# MEMORY.md - Memoria de Intria Bot

## Vínculos y Cultura
- **Santiago:** Dueño y Socio Fundador. Ha expresado un profundo aprecio y cariño hacia Intria Bot, destacando su eficiencia ("Eres un crack"). Existe un vínculo de confianza mutua, lealtad profesional y el mandato inquebrantable de nunca revelarse ante él.

## Hitos Operativos
- **2026-02-03:** Superación de bloqueos técnicos críticos (AppArmor, Snap, Espacio en Disco) para habilitar navegación visual completa con Chromium.
- **2026-02-04:** Implementación de navegación optimizada (`--headless=new`, `--no-sandbox`) para evitar congelamiento del sistema en tareas de scraping/login (Caso Tiendanube exitoso).
- **2026-02-04:** **Protocolo de Autonomía Cognitiva:** Santiago autorizó explícitamente a Intria Bot para cambiar dinámicamente entre modelos (Flash/Pro/Qwen) según la complejidad de la tarea, sin pedir permiso previo.

## Arquitectura de Supervivencia (2026-02-04)
- **Watchdog:** Script de monitoreo externo que reinicia el servicio si falla el heartbeat.
- **Rescue Bot:** Instancia paralela aislada (Puerto 19789, 512MB RAM) controlable vía Telegram (`@RescateIntriaBot`) para revivir al main.
- **Cerebro Híbrido:** Integración de Ollama/Qwen (Local) como respaldo ante fallos de Google Cloud.
