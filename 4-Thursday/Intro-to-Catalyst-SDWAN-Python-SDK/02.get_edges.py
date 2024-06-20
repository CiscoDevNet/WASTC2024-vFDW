import os
from pprint import pprint
import json
from catalystwan.session import create_manager_session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get credentials from environment variables or prompt user
url = os.getenv("SDWAN_URL") or input("URL: ")
username = os.getenv("SDWAN_USERNAME") or input("Username: ")
password = os.getenv("SDWAN_PASSWORD") or input("Password: ")

with create_manager_session(url=url, username=username, password=password) as session:
    # Get all the vEdge devices that are part of the fabric
    response = session.get("/dataservice/system/device/vedges")
    edges = json.loads(response.text)
    pprint(edges)