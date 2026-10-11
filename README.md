# MSF Automation

A Python-based tool for interacting with the [Metasploit Framework](https://www.metasploit.com/) using Python's built-in `subprocess` module.

This project demonstrates how to automate Metasploit console commands, list available exploit modules, and integrate command-line security tools into Python workflows.

## Features

- Launch Metasploit from Python.
- List available exploit modules.
- Capture console output using `subprocess`.
- Automate basic Metasploit console commands.
- Learn Python-based security tool automation.

## Requirements

- macOS or Linux
- Python 3.10+
- Metasploit Framework
- Homebrew (macOS installation method)

## 1. Install Homebrew

If Homebrew isn't installed, follow the instructions on the official website:

https://brew.sh/

Verify your installation:

```bash
brew --version
```

## 2. Install Metasploit on macOS

First, update Homebrew:

```bash
brew update
```

Search for an available Metasploit formula:

```bash
brew search metasploit
```

**Note:** Metasploit Framework may not be available as an official Homebrew formula. If the search doesn't return a suitable formula, use Rapid7's official installation instructions:

https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html

Avoid installing unverified third-party Homebrew formulas or taps.

### Verify the Installation

Check whether Metasploit is available:

```bash
msfconsole --version
```

Launch the console:

```bash
msfconsole
```

If the console opens, the installation is ready to use.

## 3. Explore Metasploit

At the Metasploit prompt, try these commands:

```text
help
version
show exploits
show auxiliary
show payloads
```

Search for exploit modules:

```text
search type:exploit
```

Exit the console:

```text
exit
```

These commands let you explore the framework and its available modules. Listing modules does not execute them.

## 4. Clone This Repository

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/msf-automation.git
```

Navigate into the project:

```bash
cd msf-automation
```

Replace `YOUR_USERNAME` with your GitHub username.

## 5. Set Up Python

Check your Python version:

```bash
python3 --version
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

The basic project uses Python's built-in `subprocess` module, so no additional Python dependencies are required.

## 6. Project Structure

```text
msf-automation/
├── README.md
├── msfconsole.py
└── .gitignore
```

## 7. Run Metasploit with Python

Create a file named `msfconsole.py`:

```python
# msfconsole.py

import subprocess


def show_exploits():
    """Display available Metasploit exploit modules."""

    try:
        result = subprocess.run(
            [
                "msfconsole",
                "-q",
                "-x",
                "show exploits; exit",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        print(result.stdout)

        if result.stderr:
            print(result.stderr)

        if result.returncode != 0:
            print(f"Metasploit exited with status {result.returncode}")

    except FileNotFoundError:
        print(
            "Metasploit was not found. "
            "Check that msfconsole is installed and in your PATH."
        )


if __name__ == "__main__":
    show_exploits()
```

Run the script:

```bash
python3 msfconsole.py
```

### How It Works

| Component | Purpose |
|---|---|
| `subprocess.run()` | Executes an external program. |
| `msfconsole` | Starts the Metasploit console. |
| `-q` | Suppresses the startup banner. |
| `-x` | Executes the supplied console command. |
| `show exploits` | Lists available exploit modules. |
| `exit` | Closes the console after the command. |
| `capture_output=True` | Captures standard output and standard error. |
| `text=True` | Returns captured output as strings. |

The script displays the modules reported by Metasploit. It does not execute an exploit against a target.

## 8. Troubleshooting

### `brew: command not found`

Homebrew may not be installed or configured correctly.

Visit https://brew.sh/ for installation instructions.

### `msfconsole: command not found`

Check whether the executable is available:

```bash
which msfconsole
```

If no path is returned, verify the installation and consult the official Metasploit documentation.

### Python Cannot Find Metasploit

If Metasploit is installed but not in your shell's `PATH`, specify the full executable path in your Python script:

```python
subprocess.run(
    [
        "/path/to/msfconsole",
        "-q",
        "-x",
        "show exploits; exit",
    ],
    check=False,
)
```

Replace `/path/to/msfconsole` with the actual path returned by your system.

### No Output Appears

Run the command directly in Terminal:

```bash
msfconsole -q -x "show exploits; exit"
```

This helps identify whether the issue comes from Metasploit or the Python script.

## 9. Security and Responsible Use

Use Metasploit only on systems you own or have explicit permission to test.

For experimentation, use an isolated lab containing intentionally vulnerable applications or virtual machines.

Listing modules is informational. Executing modules against real systems can cause service disruption or unintended changes.

## Resources

- [Metasploit Framework](https://www.metasploit.com/)
- [Official Metasploit Documentation](https://docs.metasploit.com/)
- [Rapid7](https://www.rapid7.com/)
- [Homebrew](https://brew.sh/)
- [Python subprocess Documentation](https://docs.python.org/3/library/subprocess.html)

## License

Add a `LICENSE` file if you intend to distribute this project as open-source software. Choose a license that fits your intended use.

---

**Disclaimer:** This project is intended for educational purposes, authorized security testing, and experimentation in controlled environments.
