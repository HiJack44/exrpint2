# This set of utilities is for updating the app
import requests, zipfile, os, io


def check_update(current_version, api_source):
    try:
        response = requests.get(api_source)
        response.raise_for_status()
        response = response.json()
        latest_version = response[0]['tag_name'].lstrip('v')
    except KeyError as e:
        print(f"{e} - Failed to load latest version")
    else:
        if latest_version > current_version:
            print(f"New version available: {latest_version}")
            print(f"Attempting download")
            download_update(response)

def download_update(source):
    print("Preparing download...")
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
                    safe_path = os.getcwd()
                    z.extractall(safe_path)
                    print("Files extracted.")
            except zipfile.BadZipfile as e:
                print(f"Bad zipfile: {e}")
            except PermissionError:
                print("Permission Error: No writing permission")
            except OSError as e:
                print(f"OS error has occured: {e}")
            else:
                print(f"Update complete")

