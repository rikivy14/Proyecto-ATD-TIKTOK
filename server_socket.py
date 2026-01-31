
# server_socket.py
# Simula el proceso de análisis que recibe los datos.

import socket
import os

# Configuración del Socket
HOST = '127.0.0.1'  # Dirección localhost (tu propio ordenador)
PORT = 9999       # Puerto de comunicación
FILE_NAME = 'datos_analisis_final.csv'
RECEIVED_PATH = 'Datos_Recibidos'

# Crear el directorio de recepción si no existe
os.makedirs(RECEIVED_PATH, exist_ok=True)

# 1. Crear el socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1) # Escucha una única conexión a la vez

print(f"📡 SERVIDOR ACTIVO: Escuchando en {HOST}:{PORT}...")

# 2. Aceptar la conexión del cliente
conn, addr = server_socket.accept()
print(f"✅ Conexión aceptada de {addr}")

# 3. Recibir el archivo
try:
    with open(os.path.join(RECEIVED_PATH, FILE_NAME), 'wb') as f:
        print("📥 Recibiendo archivo...")
        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            # Escribir los datos recibidos en el nuevo archivo
            f.write(data)

    print(f"🌟 ÉXITO: Archivo '{FILE_NAME}' recibido y guardado en '{RECEIVED_PATH}'.")

except Exception as e:
    print(f"❌ Error durante la recepción: {e}")

finally:
    # 4. Cerrar la conexión
    conn.close()
    server_socket.close()
    print("🔌 Servidor cerrado.")
