# Websockets and Webhooks Demo

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.7 or higher (tested on Python 3.10.14)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app
<br>

## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
cd WASTC2024-vFDW/3-Wednesday/websockets-and-webhooks
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

## WebSocket Demo

### **Introduction**: 

In this guided tutorial, we will explore the fundamentals of WebSocket communication using Python. We'll walk through several steps to set up and interact with WebSocket servers and clients, leveraging basic scripts and an admin panel for monitoring activity.

<br>

     +----------------------+            +-----------------------+            +-----------------------+
     | websocket_server.py  |            |  websocket_client.py  |            | websocket_server.html |
     +----------------------+            +-----------------------+            +-----------------------+
                    |                                |                                |
                    |                                |                                |
                    v                                v                                v
               WebSocket Server                WebSocket Client                WebSocket Server
                    |                                |                                |
                    +--------+-----------------------+----------------+---------------+
                             |                                        |
                             |                                        |
                             v                                        v
                         WebSocket                               HTTP Server
                             |                                  (http.server)
                             |                                        |
                             |                                        |
             +-----------+--------+-----------+           +--------------+-----------+
             |     websocket_client.html      |           |      admin_panel.html    |
             +--------------------------------+           +--------------------------+

<br>


**Interaction Between Files**
In this diagram (above), we'll illustrate how the various files interact with each other and with the servers.

Files:

- **websocket_server.py**: This Python script serves as the WebSocket server, handling incoming WebSocket connections and messages.
- **websocket_client.py**: The WebSocket client script interacts with the server to send and receive messages.
- **websocket_server.html**: This HTML file can be used to visualize WebSocket server activity or interact with the server through a browser interface.
- **websocket_client.html**: Represents a client-side HTML page that interacts with the WebSocket server.
- **admin_panel.html, admin_panel.js, admin_panel.css**: These files together form an admin panel that monitors WebSocket activity, displaying connected clients and message history.
- **HTTP Server (http.server)**: Serves static files such as HTML, CSS, and JavaScript files to the browser.

Modules:

- **WebSocket Server**: The server listens for incoming WebSocket connections, receives and sends messages, and logs activity.
- **WebSocket Client**: Connects to the server, sends and receives messages based on user interaction or scripts.
- **Admin Panel**: Displays client connections and message history, interacts with the WebSocket server to fetch data.
- **WebSocket Protocol**: Implements the WebSocket protocol for both server-side and client-side communication

<br>


### **Step 1**: Change directories into the **websockets** directory

```bash
cd websockets
```
<br>

### **Step 2**: Observe and run the server

- Open **python websocket_server.py** and observe it's contents. 

- Run the Server

```bash
python3 websocket_server.py
```
<br>

### **Step 3**: Open a new terminal, observe the client, and run the client

> **Note:** Every time you open a new Terminal in these labs, ensure you are in the correct directory (in this case **websockets-and-webhooks/websockets**) and that the virtual environment is also enabled in the new Terminal.
<br>

- Open **websocket_client.py** and observe it's contents. 

- Run the Client

```bash
python3 websocket_client.py
```

You should see the following output: **Received from server: Echo: Hello, World!**
<br>
<br>

### **Step 4**: Change the message the client will send

- Open **websocket_client.py** in your IDE and change line 8, inserting your own message. Don't forget to save it!
  
```
await websocket.send("<Insert your message here>")
```

- Send the new message to the server
  
```bash
python3 websocket_client.py
```

Your new message should now be displayed.


- Navigate back to the terminal where the **websocket server** is running and observe a log of all messages sent, e.g.

**Received message: Hello, World!**
<br>
**Received message: Hello, World!**
<br>
**Received message: I am good**
<br>
**Received message: Hello, World!**
<br>
**Received message: Hello, World!**
<br>
**Received message: Hello, World!**
<br>
**Received message: yo!**
<br>

- Leave the websocket server running.

  <br>

### **Step 5**: Communicate through the websocket via a browser

- Open websocket_server.**html** and observe the HTML with JavaScript code.

- In the terminal where the websocket client was running previously (websocket server should still be running in another terminal window), run the HTTP server:

```bash
python3 -m http.server
```

> **Note:** If prompted, allow incoming network connections

- Navigate in your browser of choice to [http://localhost:8000/websocket_client.html](http://localhost:8000/websocket_client.html), enter a message of your choice and click "Send". The message should be Echoed in the browser.

- Navigate to the terminal where **websocket server** is running and you should see the messages you've sent through the browser, e.g.:

**Received message: ok** 
<br>
**Received message: Adrian is a genius**
<br>
**Received message: hahaha**

<br>

### **Step 6**: Monitor WebSocket activity using the Admin Panel

With the WebSocket server running in one terminal (python3 websocket_server.py) and the HTTP server running in the other (python3 -m http.server), you can now use the Admin Panel to monitor client connections and messages in real-time.

- Prepare the Admin Panel: open the **admin_panel.html**, **js/admin_panel.js**, and **styles/admin_panel.css** files are in the IDE.

- Access the Admin Panel: Open your web browser and navigate to [http://localhost:8000/admin_panel.html](http://localhost:8000/admin_panel.html)

- Interact with the Admin Panel: Use the "Show Clients" and "Show Messages" buttons to view the list of connected WebSocket clients and the history of messages exchanged. The Admin Panel will update the statistics as new clients connect and messages are sent via the WebSocket Client at [http://localhost:8000/websocket_client.html](http://localhost:8000/websocket_client.html)

*You just need to click on 'Show Messages' a few times to see the updated list.*

- Observe Server Activity: As you interact with the Admin Panel, observe the terminal where the WebSocket server is running. You should see logs indicating that the server is processing requests from the Admin Panel, such as fetching the list of clients or retrieving message history.

### **Cleanup**

Terminate the Websocker Server and HTTP Server in their respective Terminals with Ctrl+C or similar command


### **Conclusion**

In conclusion, this tutorial has guided you through setting up and interacting with WebSocket servers and clients using Python. You've learned to modify client messages, communicate via WebSocket in a browser, and monitor activity using an admin panel. These skills are foundational for developing real-time web applications that require efficient bi-directional communication.

<br>


<br>
<br>

## Webhook Demo

### **Introduction**: 

Welcome to the Webhooks Demo! In today's interconnected digital world, webhooks play a crucial role in enabling real-time communication between applications. Unlike traditional APIs, which require continuous polling to receive updates, webhooks allow servers to push information to clients as soon as events occur. This makes webhooks an efficient and scalable solution for modern web applications, ensuring timely data exchange and seamless integration across various services.

In this demo, we'll explore how to set up and use webhooks in a Python environment. We'll walk through the entire process, from triggering events and sending HTTP POST requests to processing these events and displaying the received data. By the end of this demo, you will have a clear understanding of how webhooks work and how you can leverage them to enhance the interactivity and responsiveness of your applications.


**Workflow of the Webhooks Demo**:

- **Event Occurs**: An event, such as new data being added or a status change, occurs on the Event Source.
- **Event Triggered**: The Event Server prepares an event payload containing relevant information.
- **HTTP POST Request**: The Event Server sends an HTTP POST request to the Webhooks Endpoint of /webhook (Webhooks Receiver).
- **Webhooks Receiver**: Handle the incoming request in app.py
- **Webhooks Handler**: The Webhooks Receiver receives the POST request, validates and processes the payload, and then passes it to the Webhooks Handler.
- **Process Event**: The Webhooks Handler processes the webhook payload, potentially performing authentication or validation before further processing.
- **Application or Service Logic**: Finally, the processed data is used by the Application or Service Logic to perform actions based on the event.

<br>

### **Step 1**: Change directories into the **webhooks** directory, observe the file structure, and examine the files

```bash
cd ../webhooks
```

- In your IDE, take a look at the files in the **webhooks** directory. In VS Code, the files are in the left panel.

![image](https://github.com/xanderstevenson/websockets-and-webhooks/assets/27918923/11e30d3f-338a-40d7-b25e-8cf77468fd08)

<br>


### **Step 2**: Run the Flask application

```bash
python3 app.py
```
<br>

    
### **Step 3**: Simulate webhook events with cURL and Postman

- In a new Terminal, send a test webhook event with cURL:

> **Note:** Remember to ensure you are in the correct directory (in this case **websockets-and-webhooks/webshooks**) and that the virtual environment is also enabled in the new Terminal.


```bash
curl -X POST http://127.0.0.1:5000/webhook -H "Content-Type: application/json" -d '{"event": "new_data", "data": {"id": 123, "message": "This is a webhook event sent via cURL"}}'
```

- Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) and observe the payload sent via cURL

![image](https://github.com/xanderstevenson/websockets-and-webhooks/assets/27918923/1d1d8fda-4e2e-4704-b00d-6b276bf05774)



<br>

- Use Postman to send a second **POST** request to `http://127.0.0.1:5000/webhook` with a different JSON payload, raw, in the body. 


```json
{
   "event": "new_data",
   "data": {
       "id": 456,
       "message": "This is a webhook event sent via Postman"
   }
}
```
Don't forget to choose **POST** and click **Send**.


![image](https://github.com/xanderstevenson/websockets-and-webhooks/assets/27918923/bbf5a2c2-4e36-4f24-8fb8-8f7dfa59fa3b)

<br>

- Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) and observe the second payload sent via Postman (a refresh may be needed).

![image](https://github.com/xanderstevenson/websockets-and-webhooks/assets/27918923/f9144dd6-5f8c-4dea-a0e1-5da2f79c895b)



### **Cleanup**

Terminate the Flask Websocket app.py with Ctrl+C or similar command.


### **Conclusion**

Congratulations on completing the Webhooks Demo! Throughout this exercise, we've delved into the fundamental concepts of webhooks and their practical implementation using Python and Flask. We started by setting up a simple webhook receiver and handler, allowing us to capture and process incoming webhook events. By simulating events and observing how data flows through our system, we demonstrated the efficiency and effectiveness of webhooks in real-time communication.

This demo not only highlights the technical aspects of webhooks but also emphasizes their significance in building modern, responsive applications. By leveraging webhooks, you can ensure that your application remains up-to-date with the latest events, providing a better user experience and reducing unnecessary server load. As you move forward, consider integrating webhooks into your own projects to facilitate seamless data exchange and enhance your application's interactivity. Thank you for participating, and happy coding!
