# Intro to Rest APIs Demo

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app
<br>


## Prologue

lol

<br>

## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
cd WASTC2024-vFDW/3-Monday/Intro-to-REST-APIs
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

## Rntro to REST APIs Demo

### **Introduction**: 

Here is our file structure:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/514cab4a-8125-4eb6-a875-6eaa0c6053bd)

And here are the key files and their purpose:

- **app/main.py**: Entry point of the application.
- **app/api/example_api.py**: Example API implementation.
- **app/utils/data.py**: Utility functions for data handling.
- **app/tests/test_example_api.py**: Unit tests for the example API.

Open each of them in your IDE and observe the functions and data.


<br>


### **Step 1**: Run the Flask app

- Run the following command from within the **WASTC2024-vFDW/1-Monday/Intro-to-REST-APIs** directory:

```bash
python3 -m app.main
```
<br>

- Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and observe the output, which should look something like this:

```
{
    "message": "Welcome to the Intro to REST APIs workshop!"
}
```

- Terminate the app my entering Ctrl + C or similar command.

<br>


### **Step 2**: Unit testing our app

Let's take a step back and consider an extremely important concept in app development: testing.

The **WASTC2024-vFDW/1-Monday/Intro-to-REST-APIs/app/tests/test_example_api.py** file is included to demonstrate how to write unit tests for your REST API. Testing is an essential part of software development, ensuring that your code works as expected and helps you catch bugs early.

Here’s a detailed explanation of the **test_example_api.py** file and how to run the tests.

This file contains unit tests for the example API you created. The tests use the **pytest** framework to verify the functionality of your API endpoints.


```
import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/api/hello')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data == {"message": "Hello, world!"}
```


### Explanation

#### Importing Modules:

1. [pytest](https://docs.pytest.org/en/8.2.x/): The testing framework. 
> **Note:** open the link and take a few moments to observe the docs. Get in the habit of *at least* skimming through the Get Started, Quickstart, How To, or similar sections.
2. app: The Flask application instance from your main.py.


#### Client Fixture:

The client fixture sets up a test client using app.test_client(). This client allows you to simulate requests to the application without running a server.


#### Test Function:

- **test_hello(client**): This function tests the /api/hello endpoint.
- **client.get('/api/hello')**: Sends a GET request to the /api/hello endpoint.
- **rv.get_json()**: Parses the response data as JSON.
- **assert rv.status_code == 200**: Checks if the response status code is 200 (OK).
- **assert json_data == {"message": "Hello, world!"}**: Checks if the response data matches the expected JSON.


#### Running the Tests

```bash
pytest
```

#### Expected Output

When you run pytest, you should see output indicating that the tests passed, something like:

```
============================= test session starts =============================
platform darwin -- Python 3.x.y, pytest-6.x.x, py-1.x.x, pluggy-0.x.x
rootdir: /path/to/intro-to-rest-apis
collected 1 item                                                               

app/tests/test_example_api.py .                                          [100%]

============================== 1 passed in 0.12s ==============================
```

#### Benefits of Testing

- Ensures Correct Functionality: Automated tests verify that your code works as expected.
- Detects Bugs Early: Catch issues before they make it to production.
- Facilitates Refactoring: Safe to refactor code, knowing that tests will catch regressions.
- Improves Code Quality: Encourages writing modular and testable code.
- By running test_example_api.py, you're following best practices in software development and ensuring that you understand the importance of testing in REST API development.




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
