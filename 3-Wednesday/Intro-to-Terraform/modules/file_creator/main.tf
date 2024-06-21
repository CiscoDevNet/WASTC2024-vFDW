variable "file_name" {
  description = "The name of the file to create"
  type        = string
}

variable "file_content" {
  description = "The content of the file to create"
  type        = string
}

resource "local_file" "created_file" {
  filename = "${path.module}/${var.file_name}"
  content  = var.file_content
}

output "filename" {
  value = local_file.created_file.filename
  description = "The filename of the file created by the module."
}
