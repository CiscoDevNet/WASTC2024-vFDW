# Intro to Terraform - Lab

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
<br>

- Install Terraform:

MacOS/Linux:
```bash
sudo unzip terraform_<VERSION>_linux_amd64.zip -d /usr/local/bin/
```

Windows:
Extract the downloaded zip file and add the executable to your PATH.
<br>

- Verify Installation:

```bash
terraform -v
```
<br>


### **Step 5**: Install Docker

- Download Docker: Visit the Docker [downloads page](https://docs.docker.com/desktop/) and download the appropriate package for your operating system. Install Docker following the instructions for your operating system.

- Verify Installation:
```bash
docker --version
```

> **Note:** I'm on a Mac and I've found installing Docker Desktop is best. When I open the app on my Desktop, then Docker Engine starts automatically. 

<br>

### **Step 6**: Install Dependencies

```bash
pip3 install -r requirements.txt
```
<br>
<br>



## Intro to Teraform


### **Introduction**: 

In this demo, you will create a simple local infrastructure using Terraform and Docker. The infrastructure will include a Docker network and a Docker container running NGINX.

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
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

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
    external = 8081
  }
}
```
<br>


When finished, **main.tf** should look as such:

```
# Configure the Docker provider
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

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
    external = 8081
  }
}
```

<br>



### **Step 2**: Initilize Terraform, then plan and apply the configuration

- Initialize the Terraform working directory:
- 
```bash
terraform init -upgrade
```



<br>




- Plan and Apply the Configuration

Generate and review the execution plan:

```bash
terraform plan
```


<br>

- Apply the configuration to create the infrastructure:

```bash
terraform apply
```

Note: Type yes when prompted to confirm the apply.

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/469d2adc-8eea-4f92-a0f4-86a1f214f060)


<br>


### **Step 3**: Verify the Infrastructure

- Open your web browser and navigate to [http://localhost:8081](http://localhost:8081).
- You should see the NGINX welcome page, indicating that the Docker container is running and accessible.

<br>


### **Step 4**: Cleanup

- Destroy the created infrastructure:

```bash
terraform destroy
```

> **Note:** Type yes when prompted to confirm the destroy.

<br>

### **Conclusion**

In this lab, you learned the basics of Terraform, including how to install it, configure a provider for Docker, define infrastructure as code, and apply and destroy the configuration. Terraform, combined with Docker, provides a powerful way to manage local development environments and infrastructure consistently.

Feel free to explore more Terraform features and advanced configurations to deepen your understanding and improve your infrastructure management skills. Happy coding!

<br>

## Additional Resources

