# NETCONF & RESTCONF for Cisco IOS XE - Demo

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app

- Learners will access DevNet's [IOS XE on Cat8kv AlwaysOn sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/ios-xe-always-on) directly using the following information:

- - -
#### Sandbox details

Cat8000v Host:

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




## RESTCONF Demo

### **Introduction**: 

For the RESTCONF demo, let's focus on a different set of tasks to showcase the versatility and capabilities of RESTCONF for network management. RESTCONF uses HTTP methods to interact with network devices, making it a simpler and more accessible option for many engineers, especially those familiar with REST APIs.

RESTCONF is a protocol based on REST principles, providing a programmatic interface for accessing data defined in YANG, using standard HTTP methods. It simplifies the process of configuring and managing network devices for engineers who are already familiar with RESTful services.

In this demonstration, we will walk through several steps that highlight the power and flexibility of RESTCONF. We'll start by using a Python script to display the current configuration of interfaces on a Cat8000V router. This will give us a clear view of the device's state before we proceed to modify its configuration.

Next, we'll transition into the creation and deletion of a network interface, specifically Loopback101. This exercise will illustrate how RESTCONF can be used to make precise and controlled changes to a device's configuration, which is essential for network automation and orchestration.

Throughout this demo, we will observe best practices for interacting with network devices programmatically, including handling JSON data structures, managing HTTP requests and responses, and understanding the implications of SSL certificate verification in a non-production environment.

By the end of this demonstration, you will have a better understanding of how RESTCONF can be leveraged to automate network configuration tasks, making your network more agile and your workflow more efficient.

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

If it was successful, you'll see an output of *Interface Loopback101 created successfully.* 

<br>

- However, you may receive an error showing the interface already exists. 


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

If that is the case, you can first remove Loopback101 by running this script:


```bash
python3 delete_interface.py
```

This should result in the output *Interface Loopback101 deleted successfully.*

<br>

- Now, (if needed) you can create the interface

```bash
python3 create_interface.py
```

This should result in *Interface Loopback101 created successfully.*

<br>


### **Call to Action**: Create an interface using a Python Script and RETCONF

Try importing [cisco-ios-xe-postman-collections](https://developer.cisco.com/codeexchange/github/repo/jeremycohoe/cisco-ios-xe-postman-collections/) and practice sending requests in Postman.



<br>


### **RESTCONF Conclusion**

In this RESTCONF demo, we've explored how to interact with a Cisco IOS XE device using RESTCONF, which is a powerful protocol that leverages standard HTTP methods for network configuration and management. Through the use of Python scripts, we've demonstrated the process of displaying existing interfaces, creating a new interface, and deleting an interface when necessary.

The interface_display.py script showcased the retrieval of interface data, while create_interface.py and delete_interface.py allowed us to modify the device's configuration by adding or removing an interface. These operations are fundamental for network engineers who are looking to automate and streamline their workflows.

By successfully creating the Loopback101 interface, we've seen how RESTCONF can be used to make precise changes to a device's configuration. Conversely, the deletion script provided a way to clean up configurations, which is just as important in maintaining a manageable network environment.

It's important to note that while we've bypassed SSL certificate verification in our scripts for simplicity and learning purposes, in a production environment, proper SSL certificates should be used, and verification should be enabled to ensure secure communications with network devices.

This demo serves as a practical introduction to network automation using RESTCONF. As you become more comfortable with these concepts, you can expand upon these scripts to include error handling, logging, and integration with other systems or orchestration tools, further enhancing the capabilities and resilience of your network automation tasks.

Remember, automation is a journey, and each script you write brings you one step closer to a more efficient and reliable network. Happy automating!

<br>

## Outro


As we conclude our NETCONF & RESTCONF for Cisco IOS XE - Demo, I hope you've found the journey enlightening and empowering. We've navigated through the intricacies of network automation, explored the capabilities of NETCONF and RESTCONF, and applied these protocols to real-world scenarios using the IOS XE on Cat8kv AlwaysOn sandbox.

Throughout this demo, you've had the chance to interact directly with network devices, retrieve and modify configurations, and witness the immediate impact of your actions. These experiences are invaluable as they provide a glimpse into the potential of automation in simplifying complex network tasks.

Remember, the skills you've honed here are just the beginning. The world of network automation is vast and ever-evolving, with new tools and techniques emerging regularly. I encourage you to continue experimenting, learning, and integrating these protocols into your workflows. As you do, you'll not only increase your proficiency but also contribute to the advancement of network management practices.

Thank you for your participation and curiosity. Keep exploring, keep automating, and most importantly, keep pushing the boundaries of what's possible in networking. Until next time, happy networking!


