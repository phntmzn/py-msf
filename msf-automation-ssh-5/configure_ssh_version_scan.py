# configure_ssh_version_scan.py

import subprocess
import sys


def main():
    command = (
        "use auxiliary/scanner/ssh/ssh_version; "
        "set RHOSTS 127.0.0.1; "
        "set THREADS 1; "
        "show options; "
        "exit"
    )

    try:
        subprocess.run(
            ["msfconsole", "-q", "-x", command],
            check=False,
        )
    except FileNotFoundError:
        print("Error: msfconsole was not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
