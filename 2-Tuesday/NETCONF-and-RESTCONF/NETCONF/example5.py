#! /usr/bin/env python

from device_info import ios_xe1
from ncclient import manager, xml_

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"],
                         port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Build XML Payload for the RPC
        save_body = '<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>'

        # Send the RPC to the Device
        save_rpc = m.dispatch(xml_.to_ele(save_body))

        # Print the NETCONF Reply
        print(save_rpc)
