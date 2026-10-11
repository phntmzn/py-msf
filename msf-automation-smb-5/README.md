# MSF Automation — SMB Examples

Five Python examples for inspecting Metasploit SMB modules and checking local TCP connectivity.

## Requirements

- Python 3
- Metasploit Framework available as `msfconsole` for the first four scripts

## Scripts

- `inspect_smb_version.py` — inspect SMB version module options and info.
- `configure_smb_scan.py` — configure the module for localhost and show options; does not run the scan.
- `inspect_smb_modules.py` — search for SMB auxiliary modules.
- `inspect_smb_module_info.py` — display module information.
- `check_smb_target.py` — check TCP connectivity to port 445 using Python sockets.

## Run

```bash
python3 inspect_smb_version.py
python3 configure_smb_scan.py
python3 inspect_smb_modules.py
python3 inspect_smb_module_info.py
python3 check_smb_target.py
```

Use Metasploit only on systems you own or are explicitly authorized to assess.
