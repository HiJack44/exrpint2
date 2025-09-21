# This is the updater for exprint2. It will be run as
# separate program to download and deploy new version of the
# app.

import requests, zipfile, platform, sys
from pathlib import Path

# Setting up logger to update_log.txt
update_log_path = Path("support/update_log.txt")
update_log_file = open(update_log_path, 'w')
sys.stdout = update_log_file

# Sys argv with link to the source of new version.
# Passed from the main app
SOURCE_URL = sys.argv[1]

# This method is checking the source url
def check_source(source_url):
    print(f"Source url: {source_url}")
    print(f"Requesting response")
    response = requests.get(source_url)
    print(f"Response: {response}")
    response.raise_for_status()
    response = response.json()

    #Fetching download url
    print(f"Getting download url")
    download_url = response[0]['assets'][0]["browser_download_url"]
    print(f"Download url: {download_url}")
    download_update(download_url)


def download_update(url):
    print(f"Download url in download_update:{url}")

def deploy_files():
    ...
if __name__ == "__main__":
    check_source(SOURCE_URL)