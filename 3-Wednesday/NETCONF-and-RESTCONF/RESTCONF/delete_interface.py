import requests
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

# RESTCONF URL for the specific interface to be deleted
interface_name = "Loopback101"
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface={interface_name}"

# Set headers
headers = {
    "Accept": "application/yang-data+json",
}

# Send DELETE request to remove the specified interface
response = requests.delete(
    url,
    headers=headers,
    auth=HTTPBasicAuth(router["username"], router["password"]),
    verify=False,
)

# Check for successful status code
if response.status_code == 204:
    print(f"\n\nInterface {interface_name} deleted successfully.\n\n")
else:
    print(
        f"Failed to delete interface {interface_name}. Status code: {response.status_code}"
    )
    print(f"Response: {response.text}")
