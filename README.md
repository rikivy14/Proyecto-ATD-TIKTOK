
# 🎵 Proyecto ATD: Análisis de Viralidad (Spotify, YouTube, Last.fm)

Este sistema analiza canciones virales de TikTok, busca sus estadísticas en tiempo real en Spotify, YouTube y Last.fm, y genera una visualización 4D para entender su impacto.

## 📋 Características
- **Integración de APIs:** Conecta con 3 plataformas distintas simultáneamente.
- **Sockets TCP:** Sistema Cliente-Servidor para transmisión segura de los datos analizados.
- **Visualización 4D:** Gráfico de burbujas (Ejes: Popularidad/Vistas, Tamaño: Oyentes, Color: Antigüedad).

## 🚀 Cómo usar este código

### 1. Requisitos
Necesitas instalar las librerías necesarias:
```bash
pip install pandas spotipy requests matplotlib
```

### 2. Configuración
El archivo `config.py` está censurado por seguridad. Debes abrirlo y poner tus propias claves:
```python
CLIENT_ID = "PON_AQUI_TU_CLAVE"
# ... rellena el resto ...
```

### 3. Ejecución
1. Ejecuta `proyecto_principal.py` para descargar datos y ver el gráfico.
2. Ejecuta `server_socket.py` en una terminal (Receptor).
3. Ejecuta `client_socket.py` en otra terminal (Emisor).

