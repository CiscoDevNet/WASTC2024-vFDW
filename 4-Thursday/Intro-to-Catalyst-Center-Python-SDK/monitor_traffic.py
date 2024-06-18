from initialize_sdk_client import initialize_client


def fetch_traffic_data(client):
    try:
        traffic_data = client.sites.get_site_health()
        for entry in traffic_data["response"]:
            print(
                f"\nSite ID: {entry['siteId']}\nHealth Score: {entry['networkHealth']}\nClients: {entry['numberOfClients']}\n"
            )
    except Exception as e:
        print(f"Failed to fetch traffic data. Error: {e}")


if __name__ == "__main__":
    client = initialize_client()
    fetch_traffic_data(client)
