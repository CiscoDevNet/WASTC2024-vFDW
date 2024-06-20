#! /usr/bin/env python

from device_info import ios_xe1
from ncclient import manager
import xmltodict

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"],
                         port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Get Configuration and State Info for Interface
        netconf_reply = m.get(filter=('xpath' ,
                                      "/interfaces-state/interface[name='GigabitEthernet1']"
                                      "/statistics/out-unicast-pkts"))

        intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        intf_info = intf_details["interfaces-state"]["interface"]

        print("")
        print("Interface Details:")
        print("  Name: {}".format(intf_info["name"]))
        print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))
