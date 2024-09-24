# Flutter Installation Scripts

This repository contains scripts to download and install Flutter on Linux and Windows systems.

## Prerequisites

- Python 3.x
- `requests` library (for downloading files)
- `subprocess` module (for running shell commands)
- `pathlib` module (for handling file paths)

## Installation

### Linux

1. Clone the repository:
    ```sh
    git clone https://github.com/zimkk/Flutter-installation-Script-for-Windows-Linux.git
    cd flutter-install-scripts
    ```

2. Install required Python packages:
    ```sh
    pip install requests
    ```

3. Run the script:
    ```sh
    python flutter_linux.py
    ```

### Windows

1. Clone the repository:
    ```sh
    git clone https://github.com/zimkk/Flutter-installation-Script-for-Windows-Linux.git
    cd flutter-install-scripts
    ```

2. Install required Python packages:
    ```sh
    pip install requests
    ```

3. Run the script:
    ```sh
    python flutter_windows.py
    ```

## Usage

### Linux

- The `flutter_linux.py` script will:
  - Download the Flutter SDK tarball.
  - Extract it to `/opt/flutter`.
  - Add the Flutter binary to the system PATH by modifying the `.bashrc` file.

### Windows

- The `flutter_windows.py` script will:
  - Download the Flutter SDK zip file.
  - Extract it to `C:\flutter`.
  - Add the Flutter binary to the system PATH by modifying the environment variables.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
