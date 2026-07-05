import socket
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from generated.protocol import deserialize_message


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind(("127.0.0.1", 9000))
    except OSError as exc:
        print(f"Failed to bind to port 9000: {exc}", flush=True)
        server.close()
        raise

    server.listen(1)
    print("Server running...", flush=True)

    while True:
        try:
            conn, addr = server.accept()
        except KeyboardInterrupt:
            break

        with conn:
            print(f"Connection: {addr}", flush=True)
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk

            if data:
                msg = deserialize_message(data)
                print(f"Received: {msg}", flush=True)

    server.close()


if __name__ == "__main__":
    main()