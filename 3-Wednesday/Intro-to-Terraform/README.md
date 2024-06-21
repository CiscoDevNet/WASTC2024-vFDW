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

Welcome to our "Intro to Terraform" session! Today, we're going to explore the powerful world of Infrastructure as Code (IaC) using Terraform, a tool that allows us to define and manage infrastructure with simple, declarative code. Whether you're a network engineer or an IT educator, you'll discover how Terraform can streamline your workflows and ensure consistency across environments. Get ready to dive into a hands-on lab that will give you a taste of Terraform's capabilities without the need for any cloud providers. Let's embark on this journey to automate and innovate the way we handle our infrastructure!
<br>


## Setup steps

> **Note:** Throughout this lab, we'll be using commands beginning with **python3**, although your system may require those commands to begin with **python**

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/CiscoDevNet/WASTC2024-vFDW.git
```
```bash
cd WASTC2024-vFDW/3-Wednesday/Intro-to-Terraform
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

The goal of this lab is to use Terraform to manage local files, which will help you understand the basics of infrastructure as code without the need for cloud providers.

<br>


### **Step 1**: Populate the Terraform configuration files

- Populate **main.tf** with this configuration (don't forget to save it):

```
resource "local_file" "hello_world" {
  filename = "${path.module}/hello.txt"
  content  = "Hello, World!"
}

resource "local_file" "dynamic_file" {
  count    = var.file_count
  filename = "${path.module}/file-${count.index}.txt"
  content  = "This is file number ${count.index + 1}"
}
```
<br>

- Populate **variables.tf** with this configuration (don't forget to save it):

```
variable "file_count" {
  description = "The number of files to create"
  default     = 3
}
```
<br>


- Populate **outputs** with this configuration (don't forget to save it):

```
output "hello_world_file" {
  value = local_file.hello_world.filename
  description = "The path of the 'Hello, World!' file"
}

output "dynamic_files" {
  value = [for f in local_file.dynamic_file : f.filename]
  description = "The paths of the dynamically created files"
}
```
<br>



### **Step 2**: Initilize Terraform, then plan and apply the configuration

- Initialize the Terraform working directory:
  
```bash
terraform init
```

The results shoud look something like this:
![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/33aa631a-fcbc-412b-b729-6f672407d2b8)



<br>



- Plan and Apply the Configuration

Generate and review the execution plan:

```bash
terraform plan
```

The results shoud look something like this (truncated for brevity):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/86e095d9-5770-431e-b1be-1f4cf5312bc5)



<br>

- Apply the configuration to create the infrastructure:

```bash
terraform apply
```

Note: Type yes when prompted to confirm the apply.

The results shoud look something like this (truncated for brevity):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/a64d5308-c270-40cd-8865-ef9ce3fbc763)


<br>


### **Step 3**: Observe the results of our Terraform operations

- Three new files should have been created and populated with the following data:

1. **hello.tx**: "Hello, World!"
2. **file-0.txt**: "This is file number 1"
3. **file-1.txt**: "This is file number 2"
2. **file-2.txt**: "This is file number 3"

<br>


### **Step 4**: Cleanup

- Destroy the created infrastructure:

```bash
terraform destroy
```
> **Note:** Type yes when prompted to confirm the destroy.

<br>

The results shoud look something like this (truncated for brevity):

![image](https://github.com/CiscoDevNet/WASTC2024-vFDW/assets/27918923/7b714ab2-ddce-48ad-81cc-56e32c046ffa)

<br>

Check the directory and you should see that all of these files have been removed:

**hello.tx**
<br>
**file-0.txt**
<br>
**file-1.txt**
<br>
**file-2.txt**


<br>

You;ll notice two files remain in your directory:

1. **terraform.tfstate**

This is the Terraform state file. Terraform uses this file to keep track of the state of your managed infrastructure and configuration. When you apply your Terraform configuration, Terraform writes the state of your infrastructure to this file. This state allows Terraform to map real-world resources to your configuration, keep track of metadata, and improve performance for large infrastructures. It is also used to determine what changes need to be applied to your infrastructure when you run terraform plan or terraform apply.


2. **terraform.tfstate.backup**

This is a backup of the previous state file. Terraform automatically creates this backup file each time the state is written to the terraform.tfstate file. This happens when you successfully run terraform apply or when you run terraform refresh. The backup file ensures that you have a way to recover the previous state in case something goes wrong with the current state.


When you remove these files, you effectively delete Terraform's record of the current and previous states of your infrastructure. Without the state file, Terraform can no longer accurately determine the actual state of the resources it manages. This could lead to several issues, such as:


Terraform might try to create resources that already exist because it has no record of their existence.
Terraform might not be able to destroy resources because it doesn't know about them.
You might encounter discrepancies between your actual infrastructure and what Terraform believes the infrastructure should be.

It's generally not recommended to delete the state files unless you are intentionally trying to reset Terraform's knowledge of your infrastructure, and you are sure that the infrastructure managed by the state file is no longer needed or can be safely reconstructed. Always handle state files with care, and consider using state backends that offer state locking and versioning for better state management and safety.


<br>

### **Conclusion**

Thank you for participating in our interactive Terraform lab! By now, you should have a foundational understanding of how Terraform can be used to manage and provision infrastructure through code, even in a local context. We've seen how Terraform can create, update, and delete resources in a predictable and efficient manner. 

As you continue to explore Terraform, remember that the principles you've learned today are just the beginning. There's a vast ecosystem out there for you to harness, and the skills you've acquired will serve as a solid base for managing real-world cloud infrastructure. Keep experimenting, keep learning, and most importantly, have fun automating your infrastructure!

<br>

## Additional Resources



- You can also run Terraform on the HashiCorp SaaS platform, which has a [free tier](https://app.terraform.io/public/signup/account).

<br>

- Terraform Providers from Cisco DevNet

See the [Terraform Providers for Cisco technologies and devices be found at this URL](https://registry.terraform.io/search/providers?namespace=CiscoDevNet)


<br>

- Terraform at Cisco

At Cisco DevNet, your main hub to lean about Terraform is [Cisco with Terraform](https://developer.cisco.com/automation-terraform/).


 <br>

- Terraform and Infrastructure as Code

Visit [Terraform and Infrastructure as Code](https://developer.cisco.com/iac/) for providers, Ansible collections, NSO NEDs, and to learn how Cisco enables IaC across the entire network fabric.

<br>

- Terraform Learning Labs

The best place to practice your Terraform skills in the [DevNet Learning Labs](https://developer.cisco.com/learning/search/?contentType=track,module,lab&keyword=Terraform&sortBy=luceneScore).

