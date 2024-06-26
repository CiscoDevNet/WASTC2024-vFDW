terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe" # Replace with the actual source URL
      version = "0.5.5"
    }
    external = {
      source  = "hashicorp/external"
      version = "~> 2.0"
    }
  }
}

provider "iosxe" {
  username = "cisco"
  password = "cisco"
  url      = "https://10.10.20.176"
  insecure = true # Allow insecure HTTPS client, if necessary
  retries  = 10
}

# Define a resource to change the banner on the device
resource "iosxe_banner" "example" {
  exec_banner           = "Alex's Banner"
  login_banner          = "Alex's Login Banner"
  prompt_timeout_banner = "Alex's Prompt-Timeout Banner"
  motd_banner           = "Alex's MOTD Banner"
}