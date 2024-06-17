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


**Interaction Between Files**
In this diagram (above), we'll illustrate how the various files interact with each other and with the servers.



Modules:

- **WebSocket Server**: The server listens for incoming WebSocket connections, receives and sends messages, and logs activity.
- **WebSocket Client**: Connects to the server, sends and receives messages based on user interaction or scripts.
- **Admin Panel**: Displays client connections and message history, interacts with the WebSocket server to fetch data.
- **WebSocket Protocol**: Implements the WebSocket protocol for both server-side and client-side communication

<br>


### **Step 1**: Use a Python script to gather the running config from a router using NETCONF

First, you'll use a Python file to retrieve the running configuration from the Cat8000V running Cisco IOS XE.

- Open **display_running_config.py** in your IDE and observe the contents.

- Run that script

```bash
python3 display_running_config.py
```

- Observe the output in the Terminal, which should look something like this (*greatly* truncated for brevity):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/aaa12b16-ddbf-49e5-9410-74bc546fc9b3)

<br>


### **Step 2**: Confirm NETCONF is enabled in IOSXE running on the Cat8000v

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

### **Step 3**: Open a new terminal, observe the client, and run the client

> **Note:** Every time you open a new Terminal in these labs, ensure you are in the correct directory (in this case **websockets-and-webhooks/websockets**) and that the virtual environment is also enabled in the new Terminal.
<br>


```bash
python3 websocket_client.py
```

You should see the following output: **Received from server: Echo: Hello, World!**
<br>
<br>

### **Step 4**: Change the message the client will send

- Open **websocket_client.py** in your IDE and change line 8, inserting your own 


- Navigate back to the terminal where the **websocket server** is running and observe a log of all messages sent, e.g.



  <br>

### **Step 5**: Communicate through the websocket via a browser



> **Note:** If prompted, allow incoming network connections


<br>

### **Step 6**: Monitor WebSocket activity using the Admin Panel

With the WebSocket server running in one terminal (python3 websocket_server.py) and the HTTP server running in the other (python3 -m http.server), you can now use the 

### **Cleanup**

Termind


### **Conclusion**

In con
<br>
