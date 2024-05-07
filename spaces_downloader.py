import subprocess
import json
import os
from pathlib import Path
import time

def download_twitter_space(url, cookies_path):
    # Command to download Twitter Spaces audio and metadata
    command = [
        'twspace_dl',
        '-i', url,
        '-c', cookies_path,
        '-m',  # Download metadata
        '-o', str("metadata")
    ]

    print("Downloading data...")  # Print the command for debugging

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    if result.returncode != 0:
        print("Failed to download Twitter Space data.")
        print("Stderr:", result.stderr)  # Directly print stderr
        return None
    else:
        print("Download successful.")
        
    # Wait a bit to ensure the file system has updated
    time.sleep(3)

    
    # Find the most recently created JSON file in the directory
    json_files = list(Path('.').glob('*.json'))
    if not json_files:
        print("No JSON file found in the directory.")
        return None
    latest_json_file = max(json_files, key=os.path.getctime)
    
    return str(latest_json_file)

def extract_host_details(json_file_path):
    # Load JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Navigate through the JSON structure to find the host name
    try:
        creator_info = data['data']['audioSpace']['metadata']['creator_results']['result']
        host_name = creator_info['legacy']['name']
        
    except KeyError as e:
        print(f"Key error: {e} - Check the JSON structure.")

    return host_name



