import socket
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from generated.protocol import serialize_message


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("127.0.0.1", 9000))

        msg = {
            "id": 1,
            "text": "Hello from client"
        }

        data = serialize_message(msg)
        print(f"Sending: {msg}", flush=True)
        client.sendall(data)

    print("Client completed.", flush=True)


if __name__ == "__main__":
    main()