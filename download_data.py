import json
import requests

def download_file(url, local_filename):
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

with open('links.json') as links_file:
	links = json.load(links_file)
	
for link in links:
	file_name = 'files/' + link['date'].replace('/', '_') + '.csv'
	download_file(link['url'], file_name)