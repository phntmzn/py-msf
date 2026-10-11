# unset_module_option.py

import subprocess


def unset_module_option():
    """Set and then unset a module option."""

    commands = (
        "use auxiliary/scanner/http/title; "
        "set VERBOSE true; "
        "unset VERBOSE; "
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
    unset_module_option()
