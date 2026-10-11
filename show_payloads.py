# show_payloads.py

import subprocess


def show_payloads():
    """Display available Metasploit payloads."""

    try:
        result = subprocess.run(
            [
                "msfconsole",
                "-q",
                "-x",
                "show payloads; exit",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        print(result.stdout)

        if result.stderr:
            print(result.stderr)

        if result.returncode != 0:
            print(
                f"Metasploit exited with status "
                f"{result.returncode}"
            )

    except FileNotFoundError:
        print(
            "Metasploit was not found. "
            "Ensure msfconsole is installed and available in PATH."
        )


if __name__ == "__main__":
    show_payloads()
