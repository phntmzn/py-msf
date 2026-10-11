# configure_global.py

import subprocess


def configure_global():
    """Set a global option in Metasploit."""

    commands = (
        "setg VERBOSE true; "
        "getg VERBOSE; "
        "exit"
    )

    result = subprocess.run(
        ["msfconsole", "-q", "-x", commands],
        capture_output=True,
        text=True,
        check=False,
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print(f"Metasploit exited with status {result.returncode}")


if __name__ == "__main__":
    configure_global()
