# inspect_smb_modules.py

import subprocess


def inspect_smb_modules():
    """Search Metasploit for SMB auxiliary modules."""

    commands = "search type:auxiliary name:smb; exit"

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
    inspect_smb_modules()
