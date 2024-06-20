#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os
import time
import yaml

from datetime import datetime
from dnacentersdk import DNACenterAPI

DNAC_URL = "TBD"
DNAC_USER = "TBD"
DNAC_PASS = "TBD"

os.environ['TZ'] = 'Europe/Amsterdam'  # define the timezone for CET
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

def main():
    """
    This application will automate Day N operations, creating device inventories, using the Cisco DNA Center REST APIs
    App workflow:
        - create device inventory - hostname, device management IP address, device UUID, software version,
            device family, role, site, site UUID
        - create access point inventory - hostname, device management IP address, device UUID, software version,
            device family, role, site, site UUID
        - identify device image compliance state and create non-compliant image inventories
        - save all files to local folder, formatted using JSON and YAML
    :return:
    """

    # logging, debug level, to file {application_run.log}
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('App "inventory_collection_sdk.py" Start, ' + current_time)

    # create a DNACenterAPI "Connection Object" to use the Python SDK
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.3.3.0',
                            verify=False)

    # get the device count
    response = dnac_api.devices.TBD()
    device_count = response['response']
    logging.info('Number of devices managed by Cisco DNA Center: ' + str(device_count))

    # get the device info list
    offset = 1
    limit = 500
    device_list = []
    while offset <= device_count:
        response = dnac_api.devices.TBD(offset=offset)
        offset += limit
        device_list.extend(response['response'])
    logging.info('Collected the device list from Cisco DNA Center')

    # create device inventory [{"hostname": "", "device_ip": "","device_id": "", "version": "", "device_family": "",
    #  "role": "", "site": "", "site_id": ""},...]
    device_inventory = []
    ap_inventory = []
    for device in device_list:
        # select which inventory to add the device to
        if device.family != "Unified AP":
            device_details = {'hostname': device['hostname']}
            device_details.update({'device_ip': device['managementIpAddress']})
            device_details.update({'device_id': device['id']})
            device_details.update({'version': device['softwareVersion']})
            device_details.update({'device_family': device['type']})
            device_details.update({'role': device['role']})

            # get the device site hierarchy
            response = dnac_api.devices.TBD(identifier='uuid', search_by=device['id'])
            site = response['response']['location']
            device_details.update({'site': site})

            # get the site id
            response = dnac_api.sites.get_site(name=site)
            site_id = response['response'][0]['id']
            device_details.update({'site_id': site_id})
            device_inventory.append(device_details)
        else:
            device_details = {'hostname': device['hostname']}
            device_details.update({'device_ip': device['managementIpAddress']})
            device_details.update({'device_id': device['id']})
            device_details.update({'version': device['softwareVersion']})
            device_details.update({'device_family': device['type']})
            device_details.update({'role': device['role']})

            # get the device site hierarchy
            response = dnac_api.devices.TBD(identifier='uuid', search_by=device['id'])
            site = response['response']['location']
            device_details.update({'site': site})

            # get the site id
            response = dnac_api.sites.get_site(name=site)
            site_id = response['response'][0]['id']
            device_details.update({'site_id': site_id})
            ap_inventory.append(device_details)

    logging.info('Collected the device inventory from Cisco DNA Center')

    # save device inventory to json and yaml formatted files
    with open('inventory/device_inventory.json', 'w') as f:
        f.write(json.dumps(device_inventory))
    logging.info('Saved the device inventory to file "device_inventory.json"')

    with open('inventory/device_inventory.yaml', 'w') as f:
        f.write('device_inventory:\n' + yaml.dump(device_inventory, sort_keys=False))
    logging.info('Saved the device inventory to file "device_inventory.yaml"')

    # save ap inventory to json and yaml formatted files
    with open('inventory/ap_inventory.json', 'w') as f:
        f.write(json.dumps(ap_inventory))
    logging.info('Saved the device inventory to file "ap_inventory.json"')

    with open('inventory/ap_inventory.yaml', 'w') as f:
        f.write('ap_inventory:\n' + yaml.dump(ap_inventory, sort_keys=False))
    logging.info('Saved the device inventory to file "ap_inventory.yaml"')

    # retrieve the device image compliance state
    image_non_compliant_devices = []
    response = dnac_api.compliance.TBD(compliance_type='IMAGE', compliance_status='NON_COMPLIANT')
    image_non_compliant_list = response['response']
    for device in image_non_compliant_list:
        device_id = device['deviceUuid']
        for item_device in device_inventory:
            if device_id == item_device['device_id']:
                image_non_compliant_devices.append(item_device)
    logging.info('Number of devices image non-compliant: ' + str(len(image_non_compliant_devices)))
    logging.info('Image non-compliant devices: ')
    for device in image_non_compliant_devices:
        logging.info('    ' + device['hostname'] + ', Site Hierarchy: ' + device['site'])

    # save non compliant devices to json and yaml formatted files
    with open('inventory/non_compliant_devices.json', 'w') as f:
        f.write(json.dumps(image_non_compliant_devices))
    logging.info('Saved the image non-compliant device inventory to file "non_compliant_devices.json"')

    with open('inventory/non_compliant_devices.yaml', 'w') as f:
        f.write('non_compliant:\n' + yaml.dump(image_non_compliant_devices, sort_keys=False))
    logging.info('Saved the image non-compliant device inventory to file "non_compliant_devices.yaml"')

    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('End of Application "inventory_collection_sdk.py" Run: ' + date_time)

    return

if __name__ == '__main__':
    main()
