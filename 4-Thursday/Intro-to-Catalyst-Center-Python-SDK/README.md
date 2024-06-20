# Cisco DNA Center Day N Operations


This repo is for an application that will automate Day N operations using Cisco DNA Center APIs

**Cisco Products & Services:**

- Cisco DNA Center, devices managed by Cisco DNA Center

**Tools & Frameworks:**

- Python environment to run the application
- Cisco DNA Center Python SDK

**Usage**

This application will automate Day N operations, creating device inventories, using the Cisco DNA Center REST APIs

**"inventory_collection_sdk.py"** Python app workflow:
- create device inventory - hostname, device management IP address, device UUID, software version,
    device family, role, site, site UUID
- create access point inventory - hostname, device management IP address, device UUID, software version,
    device family, role, site, site UUID
- identify device image compliance state and create image non-compliant inventories
- save all files to local folder, formatted using JSON and YAML

Sample output:

```shell
INFO:root:App "inventory_collection_sdk.py" Start, 2022-05-18 15:34:18
INFO:root:Number of devices managed by Cisco DNA Center: 13
INFO:root:Collected the device list from Cisco DNA Center
INFO:root:Collected the device inventory from Cisco DNA Center
INFO:root:Saved the device inventory to file "device_inventory.json"
INFO:root:Saved the device inventory to file "device_inventory.yaml"
INFO:root:Saved the device inventory to file "ap_inventory.json"
INFO:root:Saved the device inventory to file "ap_inventory.yaml"
INFO:root:Number of devices image non-compliant: 3
INFO:root:Image non-compliant devices: 
INFO:root:    LO-CN, Site Hierarchy: Global/OR/LO/Floor-3
INFO:root:    LO-BN, Site Hierarchy: Global/OR/LO/Floor-3
INFO:root:    NYC-ACCESS, Site Hierarchy: Global/NY/NYC/Floor-8
INFO:root:Saved the image non-compliant device inventory to file "non_compliant_devices.json"
INFO:root:Saved the image non-compliant device inventory to file "non_compliant_devices.yaml"
INFO:root:GitHub push for file: ap_inventory.yaml
INFO:root:GitHub push for file: non_compliant_devices.json
INFO:root:GitHub push for file: ap_inventory.json
INFO:root:GitHub push for file: non_compliant_devices.yaml
INFO:root:GitHub push for file: device_inventory.json
INFO:root:GitHub push for file: device_inventory.yaml
INFO:root:End of Application "inventory_collection_sdk.py" Run: 2022-05-18 15:34:33
```
This repo is a simplified version of the one that can be found here: https://github.com/cisco-en-programmability/dnacenter_day_n. Thank you Gabi Zapodeanu for sharing this with the community!

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).


