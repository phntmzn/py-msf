# configure_module.py

import subprocess


def configure_module():
    """Configure a Metasploit module and display its options."""

    commands = (
        "use auxiliary/scanner/http/title; "
        "set VERBOSE true; "
        "show options; "
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
    configure_module()
