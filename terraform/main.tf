variable "env" {
  type    = string
  default = "prod"
}

variable "app" {
  type    = string
  default = "payment"
}


output "message" {
  value = "deploying ${var.app} in ${var.env} environment"
}
