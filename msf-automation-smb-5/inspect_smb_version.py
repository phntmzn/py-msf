# inspect_smb_version.py

import subprocess


def inspect_smb_version():
    """Inspect the SMB version module and its options."""

    commands = (
        "use auxiliary/scanner/smb/smb_version; "
        "show options; "
        "info; "
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
    inspect_smb_version()
