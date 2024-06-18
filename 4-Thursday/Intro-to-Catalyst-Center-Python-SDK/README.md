# Intro to Catalyst Center Python SDK

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app

- Learners will access DevNet's [Catalyst Center Always-On v2.3.3.6 sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/Catalyst-Center-Always-On) directly using the following information:

- - -
#### Sandbox details

Cisco Catalyst Center (Formerly known as Cisco Digital Network Architecture (DNA) Center) v2.3.3.6:

- **Public URL**: https://sandboxdnac.cisco.com
  <br>
- **Username**: devnetuser
  <br>
- **Password**: Cisco123!
  <br>
- **Notes**: 1) Accept the self-signed certificate 2) Allow browser notifications

In this sandbox, developers can:

- Interact with the Cisco Catalyst Center API calls using a variety of REST clients such as POSTMAN or CURL.
- Develop and test applications for Cisco Catalyst Center.

- - -

<br>


## Prologue

Welcome to the NETCONF & RESTCONF for Cisco IOS XE - Demo, an interactive learning experience designed to introduce you to the world of network automation using two of the most prevalent protocols in the industry: NETCONF (Network Configuration Protocol) and RESTCONF (Representational State Transfer Configuration Protocol).


<br>


## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
cd WASTC2024-vFDW/4-Thursday/Intro-to-Catalyst-Center-Python-SDK
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

## Catalyst Center Python SDK

### **Introduction**: 

Welcome, everyone! 
<br>

### **Step 1**: ?

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


### **Step 2**: ?

First, you'll use a Python script to retrieve the running configuration from the Cat8000V running Cisco IOS XE.

- Open **display_running_config.py** in your IDE and observe the contents.

- Run that script

```bash
python3 display_running_config.py
```

- Observe the output in the Terminal, which should look something like this (*greatly* truncated for brevity):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/aaa12b16-ddbf-49e5-9410-74bc546fc9b3)

<br>


### **Step 3**: ?

Now, you'll use a Python script to retrieve the hostname from the Cat8000V running Cisco IOS XE.

- Open **display_hostname.py** in your IDE and observe the contents. Now, we are suing a filter to return *only* the hostname. We also include some Python logic to handle exceptions.

```bash
python3 display_hostname.py
```

- Observe the output in the Terminal, which should look something like this (hostname may differ):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/cca9ea6b-d66a-4c6e-9638-6295f2145c04)

<br>



### **Step 4**: ?

Now, you'll use a Python script to update the hostname on the Cat8000V running Cisco IOS XE.

- Open **update_hostname.py** in your IDE and observe the contents. See the different functions for displaying and setting the hostname. Also observe the way we use input() to ask the user for a hostname.

- Run that script

```bash
python3 websocket_client.py
```

The output should look something like this:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/50551a4f-d788-4d6d-a040-b1ba3eb2a042)


<br>


### ** Conclusion**



<br>
<br>
