import requests
import json
from requests.auth import HTTPBasicAuth

# Define device information
router = {
    "host": "devnetsandboxiosxe.cisco.com",
    "port": 443,
    "username": "admin",
    "password": "C1sco12345",
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

# Print response
interfaces = response.json()
print(json.dumps(interfaces, indent=2))
