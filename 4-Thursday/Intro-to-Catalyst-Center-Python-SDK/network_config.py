import requests
from initialize_sdk_client import initialize_client


def get_network_information(client):
    try:
        url = f"{client.base_url}/dna/intent/api/v1/network"
        headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": client.access_token,
        }
        response = requests.get(
            url, headers=headers, verify=False
        )  # Assuming SSL verification is disabled
        response.raise_for_status()  # Raise an exception for 4xx/5xx errors
        network_info = response.json()["response"]
        return network_info
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving network information: {e}")
        return None


def print_network_information(network_info):
    if network_info is None:
        print("No network information available.")
        return

    print("\n\nNetwork Information:\n\n")
    for info in network_info:
        print(f"Instance UUID: {info['instanceUuid']}")
        print(f"Type: {info['type']}")
        print(f"Key: {info['key']}")
        print(f"Value: {info['value']}")
        print()


if __name__ == "__main__":
    client = initialize_client()

    # Retrieve network information
    network_info = get_network_information(client)

    # Print network information
    print_network_information(network_info)
