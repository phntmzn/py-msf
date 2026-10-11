# inspect_ssh_version.py

import subprocess
import sys


def main():
    command = (
        "use auxiliary/scanner/ssh/ssh_version; "
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
        print("Error: msfconsole was not found. Check your Metasploit installation.")
        sys.exit(1)


if __name__ == "__main__":
    main()
