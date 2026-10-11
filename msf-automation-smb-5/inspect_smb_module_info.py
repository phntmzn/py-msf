# inspect_smb_module_info.py

import subprocess


def inspect_smb_module_info():
    """Display information about the SMB version module."""

    commands = "info auxiliary/scanner/smb/smb_version; exit"

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
    inspect_smb_module_info()
