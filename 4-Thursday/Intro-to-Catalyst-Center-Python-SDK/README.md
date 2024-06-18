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

Welcome to the "Intro to Catalyst Center Python SDK" tutorial! In this tutorial, you will learn how to leverage the Cisco Catalyst Center Python SDK to interact with Cisco DNA Center's API. This SDK allows developers to automate and manage network devices and services provided by Cisco DNA Center programmatically.


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



## Catalyst Center Python SDK demo

### **Introduction**: 

Welcome to the Catalyst Center Python SDK demo! This tutorial will guide you through using the Cisco Catalyst Center Python SDK to interact with Cisco DNA Center's API. You will perform various tasks such as initializing the SDK client, retrieving device information, monitoring traffic, and fetching network configurations.


<br>

### **Step 1**: Find and observe the Docs for the SDK

When working with an SDK, one of the firat things you should do is to take a look at the docs.

- Open the docs in your browser: [Cisco Catalyst Center - Python SDK docs](https://developer.cisco.com/docs/dna-center/python-sdk-getting-started/)


<br>

We saw at the top of this README that we are using the sandbox with Catalyst Center version 2.3.3.6

- Locate docs for v2.3.3.6 and change to that version

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/1f0acf75-17b9-46f4-b54c-52a5bf366696)

<br>

- In the menu panel on the left, navigate to SDKs > Python SDK > [Quickstart](https://developer.cisco.com/docs/dna-center/2-3-3/quickstart/)

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/ea1a8e7d-2a99-41ac-a426-7ffb361be3f8)

Take a few moments and slowly scroll all the way to the bottom of the page, scanning and skimming the major sections. This will give you a broad and basic overview of what you need to consider when using the Python SDK for this version of Catalyst Center.

<br>


### **Step 2**: Initilaize the Catalyst Center client

- Open the **initilaize_sdk_client.py** file and observe its contents

Notice how the **dnacentersdk** module is imported. We installed that in our virtual environment when we used the command **pip install -r requirements.txt** previously. Also noticed how *config* is imported on line two and then used on lines 7-9:

![config](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/57c78b2c-dc5f-4c97-a7a1-43c8c558930f)


<br>

- Open **config.py** and observe what is being imported into **initilaize_sdk_client.py**.

This module importation is a great feature of Python.

<br>

- Run the Python file to initialize the Catalyst Center client

```bash
python3 initialize_sdk_client.py
```

The results in the Terminal should read **Catalyst Center client initialized successfully!**

<br>

> **Note:** The purpose of this script is to initialize a client connection to a Cisco DNA Center using the dnacentersdk Python library. This client will enable you to interact with Cisco DNA Center's API, which allows for the automation and management of network devices and services provided by Cisco DNA Center.
>
> It is your starting point for leveraging the power of Cisco DNA Center API to enhance and automate network management tasks, providing numerous benefits in terms of efficiency, reliability, and scalability.


<br>


### **Step 3**: Retrieve and Display Devices:

Now you will demonstrate how to list network devices managed by Catalyst Center, using a Python script.


- Open **display_devices.py** in your IDE and observe the contents. Notice on line 1 how it's importing the *initialize client* function from the *initialize_sdk_client.py* module. It then uses it to initialize and runs the *list_network_devices()* function to retrieve and print out the devices and their details.

```bash
python3 display_devices.py
```

- Observe the output in the Terminal, which should look something like this (device details may differ):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/075661f6-c936-4666-9938-6de901431c20)

<br>


### **Step 4**: Fetch Traffic Data


Now, you'll use a Python script to illustrate how to retrieve network traffic statistics.

- Open **monitor_traffic.py** in your IDE and observe the contents. See the different functions for displaying and setting the hostname. Also observe the way we use input() to ask the user for a hostname.

- Run that script

```bash
python3 monitor_traffic.py
```

The output should look something like this:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/b7f63b7f-f2e9-4418-b8f6-3ab3e245fedc)


<br>


### **Step 5**: Retrieve network setting and configurations

Gather structured view of various network settings and configurations managed by Cisco Catalyst Center, useful for monitoring and managing network profiles and configurations programmatically.

- Open **network_config.py** in your IDE and observe the contents. Observe the import. GET request, try/except error handling, and other components.

This script will return a list where each entry represents a specific configuration instance fetched from Cisco Catalyst Center, containing:
  
1. Instance UUID: Unique identifier for the configuration instance.
2. Type: Indicates the setting or configuration category.
3. Key: Specific setting or configuration key within the category.
4. Value: Actual value or configuration details associated with the key.

<br>

- Run that script

```bash
python3 network_config.py
```

The output should look something like this:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/c8c2f0a8-8f05-4719-b1cf-d306e15f26be)


This script is useful for network administrators or developers working with Cisco DNA Center who need to retrieve and view existing network profiles configured within their network infrastructure.

<br>


### **Conclusion**

In conclusion, this tutorial provides a comprehensive introduction to using the Cisco Catalyst Center Python SDK. By leveraging this SDK, developers can automate network management tasks, enhance operational efficiency, and gain deeper insights into network infrastructure managed by Cisco DNA Center. Start exploring and innovating with Cisco's Catalyst Center SDK today!
