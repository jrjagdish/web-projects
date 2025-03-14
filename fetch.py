
import json
import requests
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

def fectch_by_name(name):

    
    Url = f"http://api.github.com/users/{name}/events"
    data = requests.get(Url)

    if data.status_code == 404:
        logging.error("Error: Invalid username")
        return None

    if data.status_code == 200:
        store = data.json()

        json_data = json.dumps(store,indent=4)
        return json_data
    
    logging.error(f"Error occurred while fetching: {data.status_code}")
    return None        
        
   

        