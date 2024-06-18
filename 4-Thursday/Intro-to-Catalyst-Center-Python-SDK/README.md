# Intro to Catalyst Center Python SDK

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app

- Learners will access DevNet's [Catalyst Center Always-On v2.3.3.6](https://devnetsandbox.cisco.com/DevNet/catalog/Catalyst-Center-Always-On)) directly using the following information:

- - -
#### Sandbox details

Cat8000v Host:

- **Public URL**: https://sandboxdnac.cisco.com
  <br>
- **Username**: devnetuser
  <br>
- **Password**: Cisco123!
  <br>
- **Notes**:

Accept the self-signed certificate

Allow browser notifications

In this sandbox, developers can:

- Interact with the Cisco Catalyst Center API calls using a variety of REST clients such as POSTMAN or CURL.
- Develop and test applications for Cisco Catalyst Center.

- - -

<br>


## Prologue

Welcome to the NETCONF & RESTCONF for Cisco IOS XE - Demo, an interactive learning experience designed to introduce you to the world of network automation using two of the most prevalent protocols in the industry: NETCONF (Network Configuration Protocol) and RESTCONF (Representational State Transfer Configuration Protocol).

In this session, we will embark on a journey through the configuration and management of network devices using these protocols, which are integral to modern network operations. NETCONF provides a mechanism for installing, manipulating, and deleting the configuration of network devices, while RESTCONF allows for similar operations through a more web-friendly HTTP-based interface.

Our sandbox environment, the IOS XE on Cat8kv AlwaysOn sandbox, will serve as our testing ground. Here, you will have the opportunity to apply your knowledge in a safe and controlled setting, allowing you to explore the capabilities of these protocols without the risk of affecting a live network.

Before we dive into the hands-on portion of the demo, ensure you have the prerequisites in place. These include a suitable Python environment, an integrated development environment (IDE) like Visual Studio Code, and tools like Postman for API interaction. With these tools at your disposal, you'll be well-equipped to follow along with the exercises and gain practical experience with NETCONF and RESTCONF.

As we proceed, remember that the goal of this demo is not just to execute commands but to understand the principles behind them. By the end of this session, you should feel more confident in your ability to automate network configurations and appreciate the efficiency gains that can be achieved through these powerful protocols.

So, let's set up our environment, roll up our sleeves, and get ready to take a significant step toward grokking network automation.

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


### **NETCONF Conclusion**

As we wrap up the NETCONF section of our demo, let's take a moment to reflect on what we've accomplished. We've successfully connected to a Cisco IOS XE device using NETCONF, a protocol designed specifically for network configuration management. We've seen firsthand how NETCONF provides a structured and secure method for reading and writing device configurations.

Through the exercises, we've retrieved the running configuration, extracted specific details like the hostname, and even updated the device configuration. These tasks, which might have been time-consuming and prone to human error if done manually, were performed swiftly and accurately with the help of our Python scripts.

This section has demonstrated the power of automation and the efficiency that NETCONF brings to network operations. By leveraging this protocol, network engineers can automate repetitive tasks, reduce configuration errors, and ensure consistency across the network infrastructure.

As you move forward, remember that the principles and practices you've learned here can be applied to a wide range of network automation challenges. The ability to programmatically interact with network devices is a critical skill in the modern networking landscape, and mastering NETCONF is a significant step in that direction.

Keep experimenting with NETCONF, explore its full potential, and integrate it into your network automation toolkit. The knowledge you've gained today is a solid foundation for your journey toward advanced network automation.

<br>
<br>
