import requests
import json

url = "https://10.10.20.176/restconf/data/ietf-interfaces:interfaces-state/"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
    "Authorization": "Basic Y2lzY286Y2lzY28=",
}

response = requests.get(url, headers=headers, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Wrap the JSON response in another object with a string key
    output = {"json_response": json.dumps(response.json())}
    print(json.dumps(output))  # Print the wrapped JSON as a string
else:
    print(f"Error: {response.status_code}")
    exit(1)


# Generated from Operational State Interfaces request in the Postman IOX-XE collection

# import requests
# import json

# url = "https://10.10.20.175/restconf/data/ietf-interfaces:interfaces-state/"

# payload = {}
# headers = {
#     "Content-Type": "application/yang-data+json",
#     "Accept": "application/yang-data+json",
#     "Authorization": "Basic Y2lzY286Y2lzY28=",
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
