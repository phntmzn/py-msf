# check_smb_target.py

import socket


def check_smb_target(host="127.0.0.1", port=445, timeout=3):
    """Check TCP connectivity to an SMB service."""

    try:
        with socket.create_connection((host, port), timeout=timeout):
            print(f"TCP connection succeeded: {host}:{port}")

    except (OSError, TimeoutError) as exc:
        print(f"TCP connection failed: {host}:{port} ({exc})")


if __name__ == "__main__":
    check_smb_target()
