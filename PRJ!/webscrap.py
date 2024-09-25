import os
import requests

def fetchAndSaveToFile(url, path):
    # Create directory if it doesn't exist
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Fetch the URL content and save to file
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)

# url = 'https://timesofindia.indiatimes.com/'
# fetchAndSaveToFile(url, "data/times.html")
