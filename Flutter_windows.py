import os
import zipfile
import subprocess
import requests
from pathlib import Path

flutter_download_url = "https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.13.0-stable.zip"
flutter_dir = r"C:\flutter"
flutter_zip = r"C:\flutter.zip"

def download_flutter():
    response = requests.get(flutter_download_url, stream=True)
    with open(flutter_zip, 'wb') as file:
        for data in response.iter_content(1024):
            file.write(data)

def extract_flutter():
    with zipfile.ZipFile(flutter_zip, 'r') as zip_ref:
        zip_ref.extractall(flutter_dir)

def set_env_variable():
    flutter_bin = Path(flutter_dir) / "flutter" / "bin"
    env_path = os.environ.get('PATH')
    if str(flutter_bin) not in env_path:
        subprocess.run(['setx', 'PATH', f"{env_path};{flutter_bin}"], shell=True)

def cleanup():
    if os.path.exists(flutter_zip):
        os.remove(flutter_zip)

def main():
    if not os.path.exists(flutter_dir):
        os.makedirs(flutter_dir)
    download_flutter()
    extract_flutter()
    set_env_variable()
    cleanup()

if __name__ == "__main__":
    main()
