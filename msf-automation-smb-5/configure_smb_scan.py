# configure_smb_scan.py

import subprocess


def configure_smb_scan():
    """Configure SMB scan options without executing the scan."""

    commands = (
        "use auxiliary/scanner/smb/smb_version; "
        "set RHOSTS 127.0.0.1; "
        "set THREADS 1; "
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
    configure_smb_scan()
