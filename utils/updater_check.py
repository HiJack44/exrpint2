# This set of utilities is for updating the app
import requests, zipfile, io, sys, platform
from pathlib import Path

# This function checks if update is available
def check_update(current_version, api_source):
    print("Checking for updates...")
    try:
        response = requests.get(api_source)
        response.raise_for_status()
        response = response.json()
        latest_version = response[0]['tag_name'].lstrip('v')
    except KeyError as e:
        print(f"{e} - Failed to load latest version")
    except requests.exceptions.ConnectionError as e:
        print(f"No internet connection. {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout error. {e}")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong. {e}")
    else:
        if latest_version > current_version:
            print(f"New version available: {latest_version}")
            print(f"Attempting download")
            #download_update(response)
            return True
        else:
            print("Your program is up-to-date")
            return False

# Function that downloads update
def download_update(source):
    print("Preparing download...")
    cwd = Path()
    print(f"Path.cwd.resolve: {cwd.resolve()}")
    try:
        print(f"Fetching download link from source")
        download_url = source[0]['assets'][0]["browser_download_url"]
        print(f"Download URL: {download_url}")
    except (KeyError, IndexError, TypeError) as e:
        print(f"Failed to load the download link {e}")
    else:
        try:
            print(f"Requesting download URL: {download_url}")
            response = requests.get(download_url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed {e}")
        else:
            print("Download link is alive. Attempting extraction")
            try:
                with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                    print("Testing OS:")
                    if platform.system() == "Windows":
                        print("OS is Windows")
                        if getattr(sys, "frozen", False):
                            print("Sys not frozen. Getting safe_path")
                            safe_path = Path(sys.executable).resolve().parent
                            print(f"safe_path: {safe_path}")
                        else:
                            print("Sys frozen. Getting safe_path")
                            safe_path = Path(__file__).resolve().parent
                            print(f"safe_path: {safe_path}")
                    else:
                        print("OS not Windows...thank god")
                        safe_path = cwd.resolve()
                    print(f"Extracting to {safe_path}")
                    z.extractall(safe_path)
                    print(f"Files extracted to {safe_path}")
            except zipfile.BadZipFile as e:
                print(f"Bad zipfile: {e}")
            except PermissionError:
                print("Permission Error: No writing permission")
            except OSError as e:
                print(f"OS error has occured: {e}")
            else:
                print(f"Update complete")

