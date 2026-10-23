import socket, time

SERVIDOR = ("receiver", 9000)        # Docker Compose resuelve "receiver" a su IP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)                 # si el eco no llega en 1 s, se da por perdido

perdidos = 0
for i in range(1, 51):
    msg = f"hola {i}"
    t0 = time.time()
    sock.sendto(msg.encode(), SERVIDOR)          # sin bind: el SO asigna un puerto dinámico
    try:
        datos, _ = sock.recvfrom(1024)
        rtt = (time.time() - t0) * 1000
        print(f"Eco: {datos.decode()}  (RTT {rtt:.2f} ms)")
    except socket.timeout:
        perdidos += 1
        print(f"'{msg}' PERDIDO (no llegó el eco en 1 s)")

print(f"Mi puerto local era: {sock.getsockname()[1]}")
print(f"Perdidos: {perdidos} de 50")
