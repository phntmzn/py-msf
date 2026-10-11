# SSH Scanning Scripts

Five Python utilities for inspecting Metasploit SSH modules and checking SSH TCP port availability.

## Scripts

- `inspect_ssh_version.py` — displays options and information for Metasploit's SSH version scanner; does not run it.
- `inspect_ssh_login_module.py` — inspects the SSH login module's options; does not attempt authentication.
- `search_ssh_modules.py` — searches Metasploit for SSH-related modules.
- `configure_ssh_version_scan.py` — configures the SSH version scanner for `127.0.0.1` and displays options; does not run the scan.
- `check_ssh_port.py` — checks whether TCP port 22 accepts connections. No Metasploit installation is required for this script.

## Requirements

- Python 3
- Metasploit Framework for the four `msfconsole` scripts

## Usage

Run from the directory containing the scripts:

```bash
python3 inspect_ssh_version.py
python3 inspect_ssh_login_module.py
python3 search_ssh_modules.py
python3 configure_ssh_version_scan.py
python3 check_ssh_port.py
```

Check a host you own or are explicitly authorized to test:

```bash
python3 check_ssh_port.py 127.0.0.1
```

Only test systems for which you have permission. The configuration script does not execute a scan.
