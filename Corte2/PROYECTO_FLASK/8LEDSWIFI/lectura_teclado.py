import socket

ipEsp32 = "192.168.0.6"
puerto = 3306

try:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ipEsp32, puerto))
except TimeoutError as e:
    print("Tiempo de espera conexion elevado")   
    print(e)

print("Conectado al ESP32")


try:
    sock.settimeout(1)
    try:
        data = sock.recv(1024)
        if data:
            print(data.decode(errors="ignore"))
    except:
        pass

    while True:
        cmd = input("Digite 0, 1, 2, 3, 4, 5, 6, 7, 8 o q para salir: ")

        if cmd.lower() == 'q':
            break
        if len(cmd) > 0:
            sock.send(cmd[0].encode())
            print("Enviado: ",cmd[0])

            try:
                respuesta = sock.recv(1024)
                if respuesta:
                    print("ESP32: ", respuesta.decode(errors="ignore").strip())
            except:
                pass

finally:
    sock.close()
    print("Conexión cerrada")

