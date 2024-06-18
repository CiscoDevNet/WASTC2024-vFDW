from initialize_sdk_client import initialize_client


def list_network_devices(client):
    devices = client.devices.get_device_list()
    for device in devices["response"]:
        print(
            f"\nDevice ID: {device['id']},\nName: {device['hostname']},\nStatus: {device['reachabilityStatus']}\n\n"
        )


if __name__ == "__main__":
    client = initialize_client()
    list_network_devices(client)
