# inspect_ssh_login_module.py

import subprocess
import sys


def main():
    command = (
        "use auxiliary/scanner/ssh/ssh_login; "
        "show options; "
        "info; "
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
