# NETCONF & RESTCONF for Cisco IOS XE - Demo

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app

- Learners will access DevNet's [IOS XE on Cat8kv AlwaysOn sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/ios-xe-always-on) directly using the following information:

#### Cat8000v Host:

- **Public URL**: devnetsandboxiosxe.cisco.com
  <br>
- **Username**: admin
  <br>
- **Password**: C1sco12345
  <br>
- **RESTCONF port**: 443
  <br>
- **NETCONF port**: 830
  <br>
- **gRPC telemetry port**: 57500
  <br>
- **ssh port**: 22
  <br>


<br>


## Prologue

Welcome to the "Websockets and Webhooks Demo," where we will dive into the world of real-time web communication. Both Websockets and Webhooks are pivotal in enabling dynamic interactions between servers and clients, but they serve different purposes and operate in distinct ways.



<br>

## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
cd WASTC2024-vFDW/3-Wednesday//NETCONF-and-RESTCONF
```
<br>

> **Note:** Optional: In VS Code you can open all files in this repo with this command
```bash
code .
```
> **Note:** You'll then see the file manager on the left-hand side. After this, simply choose **Terminal > New Terminal** from the VS Code menu to open a new Terminal.
<br>


### **Step 2**: Create and activate a Python virtual environment

- Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
- Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```
<br>



### **Step 3**: Install Dependencies

```bash
pip3 install -r requirements.txt
```
<br>
<br>

## NETCONF Demo

### **Introduction**: 

Welcome, everyone! Today, we're going to dive into the world of network automation using NETCONF (Network Configuration Protocol) with Cisco IOS XE devices. NETCONF is a powerful protocol that allows us to programmatically manage and configure network devices, making our workflows more efficient and less error-prone. In this hands-on demo, we will explore how to use NETCONF to:

- Retrieve the running configuration of a network device.
- Extract specific configuration details, such as the hostname.
- Update the device configuration, specifically changing the hostname.

By the end of this session, you'll have a practical understanding of how to interact with network devices using NETCONF, which is a crucial skill for modern network engineers and IT professionals.*WebSocket Protocol**: Implements the WebSocket protocol for both server-side and client-side communication

<br>

### **Step 1**: Confirm NETCONF is enabled in IOSXE running on the Cat8000v

- SSH into device
```bash
ssh admin@devnetsandboxiosxe.cisco.com
```

- Provide password
```bash
C1sco12345
```

- Check is NETCONF is enabled
```bash
show running-config | include netconf
```

- If NETCONF is enabled, you will see the **netconf-yang** command in the running configuration output.

- **If** NETCONF is *not* enabled, follow these steps to enable it:

Enter Global Configuration Mode, enable NETCONF, and write to memory:

```bash
configure terminal
netconf-yang
end
write memory
```

Now, when you re-run *show running-config | include netconf*, you should see *netconf-yang* in the output.

- Terminate the SSH session
```bash
exit
```

> **Note:** *write memory* and *copy running-config startup-config* are essentially the same command on Cisco IOS devices. They both serve the purpose of saving the current running configuration (in RAM) to the startup configuration (in NVRAM), ensuring that configuration changes persist across device reboots.

<br>


### **Step 2**: Use a Python script to gather the running config from a router using NETCONF

First, you'll use a Python script to retrieve the running configuration from the Cat8000V running Cisco IOS XE.

- Open **display_running_config.py** in your IDE and observe the contents.

- Run that script

```bash
python3 display_running_config.py
```

- Observe the output in the Terminal, which should look something like this (*greatly* truncated for brevity):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/aaa12b16-ddbf-49e5-9410-74bc546fc9b3)

<br>


### **Step 3**: Use a Python script to gather the hostname from a router using NETCONF

Now, you'll use a Python script to retrieve the hostname from the Cat8000V running Cisco IOS XE.

- Open **display_hostname.py** in your IDE and observe the contents. Now, we are suing a filter to return *only* the hostname. We also include some Python logic to handle exceptions.

```bash
python3 display_hostname.py
```

- Observe the output in the Terminal, which should look something like this (hostname may differ):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/cca9ea6b-d66a-4c6e-9638-6295f2145c04)

<br>



### **Step 4**: Update and confirm the hostname with NETCONF and a Python script

Now, you'll use a Python script to update the hostname on the Cat8000V running Cisco IOS XE.

- Open **update_hostname.py** in your IDE and observe the contents. See the different functions for displaying and setting the hostname. Also observe the way we use input() to ask the user for a hostname.

- Run that script

```bash
python3 websocket_client.py
```

The output should look something like this:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/50551a4f-d788-4d6d-a040-b1ba3eb2a042)

<br>
<br>


## RESTCONF Demo

### **Introduction**: 

For the RESTCONF demo, let's focus on a different set of tasks to showcase the versatility and capabilities of RESTCONF for network management. RESTCONF uses HTTP methods to interact with network devices, making it a simpler and more accessible option for many engineers, especially those familiar with REST APIs.

<br>

### **Step 1**: Change the directory into RESTCONF

```bash
cd ../RESTCONF
```
<br>


### **Step 2**: Use a Python script with RESTCONF to display the interfaces

Here, you use a Python script to display the interfaces on the Cat8000V running Cisco IOS XE.

- Open **interface_display.py** in your IDE and observe the contents. See URI with endpoint, the headers, and the GET request needed to be sent to return the interfaces.

Observe how *response.json()* converts the JSON-formatted data from the response body into a Python dictionary (or list, depending on the JSON structure). *json.dumps* is used to serialize the Python dictionary interfaces back into a JSON-formatted string. The *indent=2* argument is used to pretty-print the JSON with an indentation level of 2 spaces, making it more human-readable.

> **Note:**
> <br>
> *json.load* reads JSON data from a file and converts it into a Python object.
> <br>
> *json.loads* reads JSON data from a string and converts it into a Python object.
> <br>
> *json.dump* writes a Python object to a file as JSON data.
> <br>
> *json.dumps* converts a Python object to a JSON string.
  

- Run that script

```bash
python3 display_interfaces.py
```

The (truncated) results should look something like this:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/18a326d1-0aa5-4231-ad94-b8a67fb9b90f)

> **Note:** You can ignore the certificate warning because we are just learning, not running in production. The reason we are getting that warning is because in our GET request, we've specified *verify=False'. However, if we set it to *True*, the script would fail until we set up a proper certificate.


<br>


### **Step 6**: Create an interface using a Python Script and RETCONF

Now, you use a Python script to create interface on the Cat8000V running Cisco IOS XE.

- Open **create_interface.py** and observe the logic. It's similar to the script to display interfaces but now we're using POST instead of GET.

- Create interface Loopback101

```
python 3create_interface.py
```

If it was successful, you'll see an output of *Interface Loopback101 created successfully." However, you may receive an error showing the interface already exists.

```
Failed to create interface. Status code: 409
Response: {
  "ietf-restconf:errors": {
    "error": [
      {
        "error-type": "application",
        "error-tag": "data-exists",
        "error-path": "/ietf-interfaces:interfaces",
        "error-message": "object already exists: /if:interfaces/if:interface[if:name='Loopback101']"
      }
    ]
  }
}
```


- If that is the case, you can first remove Loopback101 by running this script:

```bash
python3 delete_interface.py
```

This should result in the output *Interface Loopback101 deleted successfully.*


Now, (if needed) you can create the interface

```bash
python3 create_interface.py
```

This should result in *Interface Loopback101 created successfully."*



### **Conclusion**


