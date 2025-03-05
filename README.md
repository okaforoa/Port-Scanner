# Python Port Scanner

A simple multithreaded Python script to scan TCP ports on a target host. **Please use this responsibly and only scan hosts you have explicit permission to test.**

## Features

- Scans ports from 1 to 1023 by default (can be customized)
- Multithreading for faster scanning
- Outputs a list of open ports
- Easy to customize or extend with banner grabbing, service detection, etc.

## Requirements

- Python 3.x
- Standard Python libraries (`socket`, `threading`, `queue`), which come preinstalled with most Python distributions

## Installation

1. Clone or download this repository:
    ```bash
    git clone https://github.com/your-username/python-port-scanner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd python-port-scanner
    ```

That’s it! No additional Python packages are required since this script relies only on the standard library.

## Usage

1. Open the `scan.py` (or whichever filename you’ve given your script) in a text editor.
2. Change the `target` variable to the IP address or hostname you want to scan. **Ensure you have authorization to do so.**
3. Optionally adjust the port range or number of threads to suit your needs.
4. Run the script:
    ```bash
    python scan.py
    ```
5. The script will print each open port to the console and show a final list of open ports at the end.

```python
# Example snippet
target = "127.0.0.1"  # or your chosen target
port_list = range(1, 1024)

# ...
print("Open ports are:", open_ports)
