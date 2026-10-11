# inspect_module.py

import subprocess


def inspect_module():
    """Inspect a Metasploit module."""

    commands = (
        "use auxiliary/scanner/http/title; "
        "info; "
        "show options; "
        "show targets; "
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
    inspect_module()
