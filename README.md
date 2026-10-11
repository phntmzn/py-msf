MSF Automation

A Python-based tool for interacting with the Metasploit Framework using Python’s built-in subprocess module.

This project demonstrates how to automate Metasploit console commands, list available exploit modules, and integrate command-line security tools into Python workflows.

Features

* Launch Metasploit from Python.
* List available exploit modules.
* Capture console output using subprocess.
* Automate basic Metasploit console commands.
* Learn Python-based security tool automation.

Requirements

* macOS or Linux
* Python 3.10+
* Metasploit Framework
* Homebrew (macOS installation method)

1. Install Homebrew

If Homebrew isn’t installed, follow the instructions on the official website:

https://brew.sh/

Verify your installation:

brew --version

2. Install Metasploit on macOS

First, update Homebrew:

brew update

Search for an available Metasploit formula:

brew search metasploit

Note: Metasploit Framework may not be available as an official Homebrew formula. If the search doesn’t return a suitable formula, use Rapid7’s official installation instructions:

https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html

Avoid installing unverified third-party Homebrew formulas or taps.

Verify the Installation

Check whether Metasploit is available:

msfconsole --version

Launch the console:

msfconsole

If the console opens, the installation is ready to use.

3. Explore Metasploit

At the Metasploit prompt, try these commands:

help
version
show exploits
show auxiliary
show payloads

Search for exploit modules:

search type:exploit

Exit the console:

exit

These commands let you explore the framework and its available modules. Listing modules does not execute them.

4. Clone This Repository

Clone the repository:

git clone https://github.com/YOUR_USERNAME/msf-automation.git

Navigate into the project:

cd msf-automation

Replace YOUR_USERNAME with your GitHub username.

5. Set Up Python

Check your Python version:

python3 --version

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

The basic project uses Python’s built-in subprocess module, so no additional Python dependencies are required.

6. Project Structure

msf-automation/
├── README.md
├── msfconsole.py
└── .gitignore

7. Run Metasploit with Python

Create a file named msfconsole.py:

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

Run the script:

python3 msfconsole.py

How It Works

Component	Purpose
subprocess.run()	Executes an external program.
msfconsole	Starts the Metasploit console.
-q	Suppresses the startup banner.
-x	Executes the supplied console command.
show exploits	Lists available exploit modules.
exit	Closes the console after the command.
capture_output=True	Captures standard output and standard error.
text=True	Returns captured output as strings.

The script displays the modules reported by Metasploit. It does not execute an exploit against a target.

8. Troubleshooting

brew: command not found

Homebrew may not be installed or configured correctly.

Visit https://brew.sh/ for installation instructions.

msfconsole: command not found

Check whether the executable is available:

which msfconsole

If no path is returned, verify the installation and consult the official Metasploit documentation.

Python Cannot Find Metasploit

If Metasploit is installed but not in your shell’s PATH, specify the full executable path in your Python script:

subprocess.run(
    [
        "/path/to/msfconsole",
        "-q",
        "-x",
        "show exploits; exit",
    ],
    check=False,
)

Replace /path/to/msfconsole with the actual path returned by your system.

No Output Appears

Run the command directly in Terminal:

msfconsole -q -x "show exploits; exit"

This helps identify whether the issue comes from Metasploit or the Python script.

9. Security and Responsible Use

Use Metasploit only on systems you own or have explicit permission to test.

For experimentation, use an isolated lab containing intentionally vulnerable applications or virtual machines.

Listing modules is informational. Executing modules against real systems can cause service disruption or unintended changes.

Resources

* Metasploit Framework
* Official Metasploit Documentation
* Rapid7
* Homebrew
* Python subprocess Documentation

License

Add a LICENSE file if you intend to distribute this project as open-source software. Choose a license that fits your intended use.

⸻

Disclaimer: This project is intended for educational purposes, authorized security testing, and experimentation in controlled environments.
