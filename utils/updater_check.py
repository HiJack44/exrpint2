# This set of utilities is for updating the app
import requests, zipfile, io, sys, platform
from pathlib import Path

# This function checks if update is available
def check_update(current_version, api_source):
    print("Checking for updates...")
    # There we call the API and get the version
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
        # This returns true to the main if there is a new version
        if latest_version > current_version:
            print(f"New version available: {latest_version}")
            return True
        else:
            print("Your program is up-to-date")
            return False