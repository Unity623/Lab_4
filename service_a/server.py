import socket
from generated.protocol import deserialize_message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9000))
server.listen(1)

print("Server running...")

conn, addr = server.accept()
print("Connection:", addr)

data = conn.recv(1024)

msg = deserialize_message(data)
print("Received:", msg)

conn.close()