"""This module downloads any remote resources specified in links.json"""

import json
import requests

def download_file(url, local_filename):
    """Download a remote resource"""
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as file_handle:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                file_handle.write(chunk)
    return local_filename


def fetch_and_save_files():
    """Download all files from links.json"""
    with open('links.json') as links_file:
        links = json.load(links_file)

        for link in links:
            file_name = 'files/' + link['date'].replace('/', '_') + '.csv'
            download_file(link['url'], file_name)


fetch_and_save_files()
