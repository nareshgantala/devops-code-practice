from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

subscription_id = "9be9bd1a-817e-486f-9b33-1b1f79ed3727"

credential = DefaultAzureCredential()

client = ComputeManagementClient(
    credential,
    subscription_id
)

vms = client.virtual_machines.list_all()

for vm in vms:
    vm_dict = vm.as_dict()
    print(vm_dict)