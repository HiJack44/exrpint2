# This is the updater for exprint2. It will be run as
# separate program to download and deploy new version of the
# app.

import requests, zipfile, platform, sys
from pathlib import Path

SOURCE_URL = sys.argv[1]

def check_source(source_url):
    print(f"Source url: {source_url}")

def download_update():
    ...

def deploy_files():

if __name__ == "__main__":
    check_source(SOURCE_URL)