from ncclient import manager
from xml.etree import ElementTree as ET

router = {
    "host": "devnetsandboxiosxe.cisco.com",
    "port": 830,
    "username": "admin",
    "password": "C1sco12345",
}


def get_running_config():
    with manager.connect(**router, hostkey_verify=False) as m:
        netconf_filter = """
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
        </filter>
        """
        netconf_reply = m.get_config("running", filter=netconf_filter)
        return netconf_reply.xml


def get_hostname():
    with manager.connect(**router, hostkey_verify=False) as m:
        netconf_filter = """
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <hostname></hostname>
            </native>
        </filter>
        """
        netconf_reply = m.get_config("running", filter=netconf_filter)
        root = ET.fromstring(netconf_reply.xml)
        hostname_elem = root.find(
            ".//{http://cisco.com/ns/yang/Cisco-IOS-XE-native}hostname"
        )
        if hostname_elem is not None:
            hostname = hostname_elem.text.strip()
            return hostname
        else:
            print("Hostname element not found in NETCONF response.")
            return None


def update_hostname(new_hostname):
    with manager.connect(**router, hostkey_verify=False) as m:
        netconf_config = f"""
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <hostname>{new_hostname}</hostname>
            </native>
        </config>
        """
        try:
            # Edit-config operation to update the hostname
            m.edit_config(target="running", config=netconf_config)
            print(f"Hostname successfully updated to: {new_hostname}")
        except Exception as e:
            print(f"Failed to update hostname: {e}")


if __name__ == "__main__":
    print("\n\nCurrent Running Configuration:")
    print(get_running_config())

    print("\nCurrent Hostname:")
    current_hostname = get_hostname()
    print(f"Hostname: {current_hostname}")

    # Prompt user to enter a new hostname
    new_hostname = input("\nEnter a new hostname: ")

    # Update the hostname
    update_hostname(new_hostname)

    # Verify updated hostname
    print("\nUpdated Hostname:")
    updated_hostname = get_hostname()
    print(f"Hostname: {updated_hostname}\n\n")
