# show_auxiliary.py

import subprocess


def show_auxiliary():
    """Display available Metasploit auxiliary modules."""

    try:
        result = subprocess.run(
            [
                "msfconsole",
                "-q",
                "-x",
                "show auxiliary; exit",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        print(result.stdout)

        if result.stderr:
            print(result.stderr)

        if result.returncode != 0:
            print(f"Metasploit exited with status {result.returncode}")

    except FileNotFoundError:
        print(
            "Metasploit was not found. "
            "Ensure msfconsole is installed and available in PATH."
        )


if __name__ == "__main__":
    show_auxiliary()
