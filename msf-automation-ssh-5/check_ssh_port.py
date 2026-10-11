# check_ssh_port.py

import socket
import sys


def check_ssh_port(host="127.0.0.1", port=22, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            print(f"TCP port {port} is open on {host}.")
            return True
    except socket.timeout:
        print(f"Connection timed out: {host}:{port}")
    except ConnectionRefusedError:
        print(f"TCP port {port} is closed on {host}.")
    except OSError as error:
        print(f"Connection failed: {error}")

    return False


if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    check_ssh_port(host)
