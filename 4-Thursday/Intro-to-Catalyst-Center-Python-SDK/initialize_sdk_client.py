from dnacentersdk import DNACenterAPI
import config


def initialize_client():
    client = DNACenterAPI(
        base_url=config.API_URL,
        username=config.USERNAME,
        password=config.PASSWORD,
        version="2.2.3.3",
        verify=False,  # Disable SSL verification
    )
    return client


if __name__ == "__main__":
    client = initialize_client()
    print("\n\nCatalyst Center client initialized successfully!\n\n")
