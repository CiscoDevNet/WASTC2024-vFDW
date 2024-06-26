terraform {
  required_providers {
    external = {
      source  = "hashicorp/external"
      version = "~> 2.0"
    }
    iosxe = {
      source  = "ciscodevnet/iosxe"
      version = "0.5.5"
    }
  }
}

provider "iosxe" {
  username = "cisco"
  password = "cisco"
  url      = "https://10.10.20.176"
  insecure = true // Set to false in production for secure connections
}

data "external" "interface_state" {
  program = ["python", "${path.module}/get_interface_state.py"]
}

output "interface_state" {
  value = data.external.interface_state.result.json_response
}
