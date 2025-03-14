import json
from fetch import fectch_by_name
import logging

logging.basicConfig(level=logging.INFO)

def display_git(name):
   events = json.loads(name)
   commits = 0
   issues = 0
   starred = 0
   if not events:
        logging.info("No events found.")
        return   
   
   if events:
      for event in events[:5]:
         event_type = event.get('type')
         
       
         
         repo_name = event["repo"]["name"]
         logging.info(f"{event_type} in {repo_name}")
            
  
     

   return name
    
        