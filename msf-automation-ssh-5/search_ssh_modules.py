# search_ssh_modules.py

import subprocess
import sys


def main():
    command = "search ssh; exit"

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
