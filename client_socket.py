# client_socket.py
# Simula el proceso de transmisión de datos.

import socket
import os
import time

# Configuración del Socket (Debe coincidir con el Servidor)
HOST = '127.0.0.1'  
PORT = 9999      
SOURCE_FILE = 'datos_analisis_final.csv'

# 1. Crear el socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Conectarse al servidor
try:
    print(f"📡 CLIENTE: Intentando conectar a {HOST}:{PORT}...")
    client_socket.connect((HOST, PORT))
    print("✅ Conexión establecida.")
    
    # 3. Leer y enviar el archivo
    if not os.path.exists(SOURCE_FILE):
        print(f"❌ ERROR: Archivo fuente no encontrado en {SOURCE_FILE}.")
        exit()

    with open(SOURCE_FILE, 'rb') as f:
        print(f"📤 Enviando archivo '{SOURCE_FILE}'...")
        while True:
            # Leer el archivo en bloques de 1024 bytes
            bytes_read = f.read(1024)
            if not bytes_read:
                break # Fin del archivo
            
            # Enviar los datos al servidor
            client_socket.sendall(bytes_read)

    print("🌟 ÉXITO: Archivo enviado completamente.")
    
    # Pequeña pausa para asegurar que el servidor termina de procesar
    time.sleep(1) 

except ConnectionRefusedError:
    print("❌ ERROR: La conexión fue rechazada. Asegúrese de que el Servidor esté activo primero.")

except Exception as e:
    print(f"❌ Error durante la transmisión: {e}")

finally:
    # 4. Cerrar la conexión
    client_socket.close()
    print("🔌 Cliente cerrado.")