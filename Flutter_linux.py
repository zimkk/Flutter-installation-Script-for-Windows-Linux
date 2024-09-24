import os
import zipfile
import subprocess
import requests
from pathlib import Path

flutter_download_url = "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.13.0-stable.tar.xz"
flutter_dir = "/opt/flutter"
flutter_tar = "/tmp/flutter.tar.xz"

def download_flutter():
    response = requests.get(flutter_download_url, stream=True)
    with open(flutter_tar, 'wb') as file:
        for data in response.iter_content(1024):
            file.write(data)

def extract_flutter():
    subprocess.run(['tar', '-xf', flutter_tar, '-C', '/opt'])

def set_env_variable():
    flutter_bin = Path(flutter_dir) / "flutter" / "bin"
    env_path = os.environ.get('PATH')
    if str(flutter_bin) not in env_path:
        bashrc_path = Path.home() / ".bashrc"
        with open(bashrc_path, 'a') as file:
            file.write(f'\nexport PATH="$PATH:{flutter_bin}"')
        subprocess.run(['source', bashrc_path], shell=True)

def cleanup():
    if os.path.exists(flutter_tar):
        os.remove(flutter_tar)

def main():
    if not os.path.exists(flutter_dir):
        os.makedirs(flutter_dir)
    download_flutter()
    extract_flutter()
    set_env_variable()
    cleanup()

if __name__ == "__main__":
    main()
