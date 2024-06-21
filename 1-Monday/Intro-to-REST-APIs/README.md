# Intro to Rest APIs - Lab

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Postman](https://www.postman.com/), either in the browser or desktop app
<br>


## Prologue

This repository contains a hands-on demonstration of REST APIs using Python and Flask. You will explore basic API functionality, learn about unit testing, and gain practical insights into building and testing RESTful services.

<br>

## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
```
```bash
cd WASTC2024-vFDW/1-Monday/Intro-to-REST-APIs
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

## Intro to REST APIs Demo

## First part of Demo

### **Introduction**: 

This demo showcases a simple Flask application that exposes RESTful APIs for basic functionalities such as retrieving a random quote and performing calculations. Here's an overview of the project structure:

<br>

Here is our file structure:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/e0fe1066-1478-479c-af8d-e2763a9afc6f)

<br>

And here are the key files and their purpose:

- **main.py**: Entry point of the application.
- **/api/example_api.py**: Example API implementation.
- **utils/data.py**: Utility functions for data handling.
- **/tests/test_example_api.py**: Unit tests for the example API.

Open each of them (in the **/app** directory) in your IDE and observe the functions and data.


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

<br>

- Now, instead of just a static message from **main.py**, let's import data from a function in another module.

In **main.py**, uncomment lines 4 and 16, save the file and reload the webpage (you may need to do it twice). The results should now be:

```
{
    "message": "Welcome to the Intro to REST APIs workshop!",
    "sample_data": {
        "data": "This is some sample data."
    }
}
```

<br>

- Terminate the app my entering Ctrl + C or similar command.

<br>


### **Step 2**: Unit testing our app

Let's take a step back and consider an extremely important concept in app development: testing.

The **/tests/test_example_api.py** files in app and app2 are included to demonstrate how to write unit tests for your REST API. Testing is an essential part of software development, ensuring that your code works as expected and helps you catch bugs early.

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

<br>

#### Client Fixture:

The client fixture sets up a test client using app.test_client(). This client allows you to simulate requests to the application without running a server.

<br>

#### Test Function:

- **test_hello(client**): This function tests the /api/hello endpoint.
- **client.get('/api/hello')**: Sends a GET request to the /api/hello endpoint.
- **rv.get_json()**: Parses the response data as JSON.
- **assert rv.status_code == 200**: Checks if the response status code is 200 (OK).
- **assert json_data == {"message": "Hello, world!"}**: Checks if the response data matches the expected JSON.

<br>

#### Running the Tests

```bash
pytest
```

<br>

#### Expected Output

When you run pytest, you should see output indicating that the tests passed, something like:

```
==================================== test session starts ====================================
platform darwin -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/alexstev/WASTC2024-vFDW/1-Monday/Intro-to-REST-APIs
collected 2 items                                                                           

app/tests/test_example_api.py .                                                       [ 50%]
app2/tests/test_example_api.py .                                                      [100%]

===================================== 2 passed in 0.24s =====================================
```

<br>

#### Benefits of Testing

- Ensures Correct Functionality: Automated tests verify that your code works as expected.
- Detects Bugs Early: Catch issues before they make it to production.
- Facilitates Refactoring: Safe to refactor code, knowing that tests will catch regressions.
- Improves Code Quality: Encourages writing modular and testable code.
- By running test_example_api.py, you're following best practices in software development and ensuring that you understand the importance of testing in REST API development.

<br>


## Second part of Demo

### **Introduction**: 

> **Note:** From this point on, we will be dealing with files in the **/app2** directory.

Welcome to Part 2 of the Intro to REST APIs Demo! In this section, we will explore additional functionalities and enhancements to our Flask application. Building upon the foundation from Part 1, we'll delve deeper into interactive features and showcase practical use cases of RESTful APIs.

<br>

### **Step 1**: Observe the new code for this part


- Open **/app2/main.py** and observe it's contents.
- Open **index.html** and observe it's contents.

<br>

### **Step 2**: Run the new Flask app

```bash
python3 -m app2.main
```

- Navigate back to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and observe the output, which should look something like this:

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/b2188d20-d30d-40d9-b8d3-1b0d7681faa1)

- Clicking on "Get Quote" will produce a random quote from **main.py** 

- Clicking on "Calculate" after entering numbers and choosing the operation, will output the results of the calculation. This is based on logic located at the end of index.html


### **Cleanup**

Terminate the Flask App in the Terminal with Ctrl+C or similar command


### **Conclusion**

This workshop introduced you to the fundamentals of REST APIs using Python and Flask. By exploring basic API functionalities, testing strategies, and enhancements, you've gained practical insights into building and testing RESTful services. Further exploration and experimentation with the provided code will solidify your understanding of REST API concepts and their application in real-world scenarios.

<br>

## Additional Resources

[WASTC-vFDW](https://www.postman.com/alexstev/workspace/wastc-vfdw/)

- This workspace in Postman demonstrates the basic functionality of REST APIs

- Postman can be run in a web browser or as a standalone app

- It’s pronounced Postman, not Postman

- Have a look!
