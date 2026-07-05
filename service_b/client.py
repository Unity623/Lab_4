import socket
from generated.protocol import serialize_message

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9000))

msg = {
    "id": 1,
    "text": "Hello from client"
}

data = serialize_message(msg)

client.send(data)
client.close()