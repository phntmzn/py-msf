# unset_global_option.py

import subprocess


def unset_global_option():
    """Set and then unset a global Metasploit option."""

    commands = (
        "setg VERBOSE true; "
        "getg VERBOSE; "
        "unsetg VERBOSE; "
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
    unset_global_option()
