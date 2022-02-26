import socket
import sys

buffer_size = 1024

host, port, send_message = sys.argv[1:]

with socket.socket() as sock:
    sock.connect((host, int(port)))
    sock.send(send_message.encode())

    response = sock.recv(buffer_size).decode()
    print(response)
