import requests
import json
from requests.auth import HTTPBasicAuth
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3 needed for this case.
warnings.simplefilter("ignore", InsecureRequestWarning)

# Define device information
router = {
    "host": "10.10.20.175",
    "port": 443,
    "username": "cisco",
    "password": "cisco",
}

# RESTCONF URL for interfaces
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"

# Set headers
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Send GET request
response = requests.get(
    url,
    headers=headers,
    auth=HTTPBasicAuth(router["username"], router["password"]),
    verify=False,
)

# Check response status code
if response.status_code == 200:
    try:
        # Attempt to parse JSON response
        interfaces = response.json()
        print(json.dumps(interfaces, indent=2))
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response content: {response.text}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Response content: {response.text}")
