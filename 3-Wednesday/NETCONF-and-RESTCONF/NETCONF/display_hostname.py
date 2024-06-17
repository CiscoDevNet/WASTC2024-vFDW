from ncclient import manager
from xml.etree import ElementTree as ET

router = {
    'host': 'devnetsandboxiosxe.cisco.com',
    'port': 830,
    'username': 'admin',
    'password': 'C1sco12345'
}

def get_hostname():
    with manager.connect(**router, hostkey_verify=False) as m:
        # NETCONF filter to retrieve only the hostname
        netconf_filter = """
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <hostname></hostname>
            </native>
        </filter>
        """
        try:
            netconf_reply = m.get_config('running', filter=netconf_filter)
            # Parse the XML response to extract the hostname
            root = ET.fromstring(netconf_reply.xml)
            hostname_elem = root.find('.//{http://cisco.com/ns/yang/Cisco-IOS-XE-native}hostname')
            if hostname_elem is not None:
                hostname = hostname_elem.text.strip()
                return hostname
            else:
                print("Hostname element not found in NETCONF response.")
                return None
        except Exception as e:
            print(f"Failed to retrieve hostname: {e}")
            return None

if __name__ == '__main__':
    hostname = get_hostname()
    if hostname:
        print(f'\n\nHere is the HOSTNAME returned from the NETCONF request:\n\n{hostname}\n\n')
    else:
        print("Failed to retrieve hostname.")
