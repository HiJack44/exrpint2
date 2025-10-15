# This is the updater for exprint2. It will be run as
# separate program to download and deploy new version of the
# app.
import json
import subprocess
import requests, zipfile, platform, sys, io
from pathlib import Path

# Setting up logger to update_log.txt
update_log_path = Path("support/update_log.txt")
update_log_file = open(update_log_path, "w")
sys.stdout = update_log_file

# Sys argv with link to the source of new version.
# Passed from the main app
SOURCE_URL = sys.argv[1]


# This method is checking the source url
def check_source(source_url):
    """

    :param source_url: The source of the update zipfile
    :return: It starts download function if everything is ok
    """

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

    # Fetching download url
    print(f"Getting download url")
    try:
        download_url = response[0]["assets"][0]["browser_download_url"]
        print(f"Download url: {download_url}")
    except (KeyError, IndexError, TypeError) as e:
        print(f"Failed to load the download link: {e}")
    else:
        download_update(download_url)


# This function will download the zipfile from the target URL
def download_update(url):
    """

    :param url: It gets the download URL
    :return: It starts the deployment of the downladed zipfile
    """
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
    """

    :param zip_file: Actually downloads the zipfile from source
    :return: Testing the OS and overwriting the existing files.
    Saving the new files on the disk. Calling the main app
    """
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
        #start_app(safe_path)
        config_check(safe_path)


# This function is checking if there is a new configuration file after update.
def config_check(path):
    main_path = path  # Path to main folder
    print(f"Main path: {main_path}")
    templates_path = main_path / "templates"  # Path to templates
    print(f"Templates path: {templates_path}")
    if templates_path / "config.json" and templates_path / "new_config.json":
        print(f"Config.json and new_config.json in {templates_path}")
        # Loading old config data
        with open(templates_path / "config.json", "r", encoding="utf-8") as oc:
            old_config = json.load(oc)
        # Loading new config data
        with open(templates_path / "new_config.json", "r", encoding="utf-8") as nc:
            new_config = json.load(nc)
        # Comparing files and adding new data to old config data
        for key in new_config:
            print(f"Loading new_config key: {key}")
            if key not in old_config:
                print(f"Adding {key} to old_config")
                old_config[key] = new_config[key]
        print(old_config, templates_path)
        write_config_changes(old_config, templates_path, main_path)
    else:
        print(f"Missing file in {templates_path}")
        start_app(main_path)


def write_config_changes(config_data, templates, main_path):
    """

    :param config_data: New data for old config
    :return: rewrites the config.json file
    :param templates: Templates folder with config.json
    """
    with open(templates / "config.json", "w", encoding="utf-8") as c:
        print(f"Dumping data to {templates}")
        json.dump(config_data, c, indent=2)

    start_app(main_path)


def start_app(path):
    """

    :param path: Path to the main app executable
    :return: Starts the main app
    """
    print("Restarting the main app")
    print(f"Path to main folder: {path}")
    if platform.system() == "Windows":
        if getattr(sys, "frozen", False):
            print("Running the exprint2.exe file")
            subprocess.Popen(str(path / "exprint2.exe"))
        else:
            print("Running the python file")
            subprocess.Popen(["python3", "main.py"])
    else:
        print("Running non windows python file")
        subprocess.Popen(["python3", "main.py"])


if __name__ == "__main__":
    check_source(SOURCE_URL)
