# Intro to Rest APIs - Lab

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 or higher (tested on Python 3.10.14 and 3.11.9)
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Terraform](https://www.terraform.io/) installed on your system.
- [Docker](https://www.docker.com/) installed on your system.
<br>


## Prologue

Terraform is an open-source tool that allows you to define and provision infrastructure using a simple, declarative configuration language. This lab will guide you through the basics of Terraform, from installation to creating a simple local infrastructure using Docker.
<br>


## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
```
```bash
cd WASTC2024-vFDW/3-Monday/Intro-to-Terraform
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


### **Step 4**: Install Terraform

- Download Terraform: Visit the Terraform [downloads page](https://developer.hashicorp.com/terraform/install) and download the appropriate package for your operating system.

- Install Terraform:

MacOS/Linux:
```bash
sudo unzip terraform_<VERSION>_linux_amd64.zip -d /usr/local/bin/
```

Windows:
Extract the downloaded zip file and add the executable to your PATH.


1Verify Installation:

```bash
terraform -v
```


### **Step 4**: Install Docker

- Download Docker: Visit the Docker [downloads page](https://docs.docker.com/desktop/) and download the appropriate package for your operating system. Install Docker following the instructions for your operating system.

- Verify Installation:
```bash
docker --version
```

> **Note:** I'm on a Mac and I've found installing Docker Desktop is best. When I open the app on my Desktop, then Docker Engine starts automatically. 



### **Step 5**: Install Dependencies

```bash
pip3 install -r requirements.txt
```
<br>
<br>



## Intro to Teraform


### **Introduction**: 

In this demo, you will create a simple local infrastructure using Terraform and Docker. The infrastructure will include a Docker network and a Docker container running Nginx.

<br>


### **Step 1**: Change to the Working Directory and populate the configuration with the Terraform provider

- Change into the working directory

```bash
cd terraform-docker-demo
```
<br>

- Copy this **provider info** into **main.tf** (don't forget to save it):

```
# Configure the Docker provider
provider "docker" {
  host = "unix:///var/run/docker.sock"
}
```
<br>

- Copy this **network configuration** info into **main.tf** (don't forget to save it):

```
# Define a Docker network
resource "docker_network" "demo_network" {
  name = "demo-network"
}
```
<br>

- Copy this **container configuration** info into **main.tf** (don't forget to save it):

```
# Define a Docker container running Nginx
resource "docker_container" "nginx" {
  image = "nginx:latest"
  name  = "demo-nginx"

  networks_advanced {
    name = docker_network.demo_network.name
  }

  ports {
    internal = 80
    external = 8080
  }
}
```
<br>


When finished, **main.tf** should look as such:

```
# Configure the Docker provider
provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Define a Docker network
resource "docker_network" "demo_network" {
  name = "demo-network"
}

# Define a Docker container running Nginx
resource "docker_container" "nginx" {
  image = "nginx:latest"
  name  = "demo-nginx"

  networks_advanced {
    name = docker_network.demo_network.name
  }

  ports {
    internal = 80
    external = 8080
  }
}
```




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
============================= test session starts =============================
platform darwin -- Python 3.x.y, pytest-6.x.x, py-1.x.x, pluggy-0.x.x
rootdir: /path/to/intro-to-rest-apis
collected 1 item                                                               

app/tests/test_example_api.py .                                          [100%]

============================== 1 passed in 0.12s ==============================
```

<br>

#### Benefits of Testing

- Ensures Correct Functionality: Automated tests verify that your code works as expected.
- Detects Bugs Early: Catch issues before they make it to production.
- Facilitates Refactoring: Safe to refactor code, knowing that tests will catch regressions.
- Improves Code Quality: Encourages writing modular and testable code.
- By running test_example_api.py, you're following best practices in software development and ensuring that you understand the importance of testing in REST API development.

<br>


## First part of Demo

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
