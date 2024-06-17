import ncclient
from ncclient import manager

router = {
    'host': 'devnetsandboxiosxe.cisco.com',
    'port': 830,
    'username': 'admin',
    'password': 'C1sco12345'
}

with manager.connect(**router, hostkey_verify=False) as m:
    netconf_reply = m.get_config('running')

print(f'\n\nHere is the RUNNING CONFIG returned from the NETCONF request:\n\n{netconf_reply}\n\n')
