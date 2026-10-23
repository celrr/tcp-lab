import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # SOCKET: UDP = SOCK_DGRAM
sock.bind(("0.0.0.0", 9000))                              # BIND: puerto 9000 (registrado)
print("Servidor UDP escuchando en el puerto 9000")

while True:
    datos, origen = sock.recvfrom(1024)                   # RECVFROM: datos + (IP, puerto) del cliente
    print(f"Recibido de {origen}: {datos.decode()}")
    sock.sendto(datos, origen)                            # SENDTO: lo devuelve al mismo cliente
