import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3 needed
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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

# Define the new interface data
interface_name = "Loopback101"  # Replace with the desired interface name
new_interface_data = {
    "ietf-interfaces:interface": {
        "name": interface_name,
        "description": "Created by RESTCONF for WASTC2024-vFDW.",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [{"ip": "10.10.10.100", "netmask": "255.255.255.0"}]
        },
    }
}

# Send POST request to create a new interface
response = requests.post(
    url,
    headers=headers,
    auth=HTTPBasicAuth(router["username"], router["password"]),
    data=json.dumps(new_interface_data),
    verify=False,
)

# Check for successful status code
if response.status_code == 201:
    print(f"\n\nInterface {interface_name} created successfully.\n\n")
else:
    print(
        f"Failed to create interface {interface_name}. Status code: {response.status_code}"
    )
    print(f"Response: {response.text}")
