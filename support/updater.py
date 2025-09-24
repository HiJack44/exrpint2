# This is the updater for exprint2. It will be run as
# separate program to download and deploy new version of the
# app.
import subprocess
import requests, zipfile, platform, sys, io
from pathlib import Path

# Setting up logger to update_log.txt
update_log_path = Path("support/update_log.txt")
update_log_file = open(update_log_path, 'w')
sys.stdout = update_log_file

# Sys argv with link to the source of new version.
# Passed from the main app
SOURCE_URL = sys.argv[1]
#APP_URL = sys.argv[2]

# This method is checking the source url
def check_source(source_url):
    print(f"Source url: {source_url}")
    print(f"Requesting response")
    try:
        response = requests.get(source_url)
        print(f"Response: {response}")
        response.raise_for_status()
        response = response.json()
    except requests.exceptions.ConnectionError as e:
        print(f"No internet connection. Update aborted. {e}")
    except requests.exceptions.Timeout as e:
        print(f"Failed to load in time: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")

    #Fetching download url
    print(f"Getting download url")
    try:
        download_url = response[0]['assets'][0]["browser_download_url"]
        print(f"Download url: {download_url}")
    except (KeyError, IndexError, TypeError) as e:
        print(f"Failed to load the download link: {e}")
    else:
        download_update(download_url)

# This function will download the zipfile from the target URL
def download_update(url):
    print(f"Download url in download_update:{url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")
    parent = Path()
    print(f"{parent.resolve()}")
    deploy_files(response)

# This function is managing file extraction and replacement
def deploy_files(zip_file):
    print(f"Preparing to deploy file from {zip_file}")

    # OS check and exe check for Windows
    print(f"Testing OS:")
    if platform.system() == "Windows":
        print("System is Windows")
        if getattr(sys, "frozen", False):
            print("Sys not frozen. Getting safe_path")
            safe_path = Path(sys.executable).resolve().parent.parent
            print(f"Safe_path: {safe_path}")
        else:
            print("Sys not frozen. Getting safe_path")
            safe_path = Path(__file__).resolve().parent.parent
            print(f"Safe_path {safe_path}")
    else:
        print("System is not Windows")
        safe_path = Path().resolve()
    print(f"Extracting files to {safe_path}")

    # File extraction into target folders
    try:
        print(f"Preparing to extract {zipfile}")
        with zipfile.ZipFile(io.BytesIO(zip_file.content)) as z:
            print(f"Attempting extraction to {safe_path}")
            z.extractall(safe_path)
            print(f"Files extracted successfully")
    except zipfile.BadZipFile as e:
        print(f"Bad zipfile: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    else:
        print("Update complete")
        start_app(safe_path)

def start_app(path):
    print("Restarting the main app")
    print(f"Path to main folder: {path}")
    if platform.system() == "Windows":
        if getattr(sys, "frozen", False):
            print("Running the exprint2.exe file")
            subprocess.Popen(str(path/"exprint2.exe"))
        else:
            print("Running the python file")
            subprocess.Popen(["python3", "main.py"])
    else:
        print("Running non windows python file")
        subprocess.Popen(["python3", "main.py"])

def config_check():
    ...

if __name__ == "__main__":
    check_source(SOURCE_URL)