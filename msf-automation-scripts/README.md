# MSF Automation Scripts

Five Python examples for running Metasploit console configuration and inspection commands through `subprocess`.

## Requirements

- Python 3
- Metasploit Framework installed and `msfconsole` available in your `PATH`

## Scripts

- `configure_module.py` — select an HTTP title auxiliary module, set `VERBOSE`, and show options.
- `configure_global.py` — set and inspect a global option.
- `unset_module_option.py` — set and unset a module option.
- `unset_global_option.py` — set and unset a global option.
- `inspect_module.py` — display module information, options, and targets.

## Run

```bash
python3 configure_module.py
python3 configure_global.py
python3 unset_module_option.py
python3 unset_global_option.py
python3 inspect_module.py
```

Each script starts a new Metasploit process. Settings generally do not persist between separate invocations.

Use Metasploit only on systems you own or are explicitly authorized to test.
