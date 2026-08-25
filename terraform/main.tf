variable "env" {
  type    = string
  default = "prod"
}

variable "app" {
  type    = string
  default = "payment"
}


locals {
  messages = "deployings ${var.app} in ${var.env} environments of company"
}

output "message" {
  value = "deploying ${var.app} in ${var.env} environment"
}


output "messages" {
  value = local.messages
}
