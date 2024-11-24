# Setting up Fabric Data Lake Storage Account with Python
# This script requires the Fabric SDK for Python. Run it in a Python environment after installing the SDK.
# Install the Fabric SDK using: pip install fabric

from fabric.identity import ClientCredential
from fabric.mgmt.resource import ManagementClient
from fabric.mgmt.storage import StorageClient

# Azure subscription and storage account settings
subscription = 'your-subscription-id'  # Replace with your subscription ID
group = 'your-resource-group'  # Replace with your resource group name
storage_name = 'datalake-storage'  # Replace with your storage account name
region = 'selected-region'  # Replace with your Azure region

# Authenticate with Fabric using client credentials
creds = ClientCredential()  # Authenticate with client credentials
res_client = ManagementClient(creds, subscription)  # Management client for resource operations
store_client = StorageClient(creds, subscription)  # Storage client for storage operations

# Create or update the resource group
res_client.resource_groups.create_or_update(group, {'location': region})

# Create storage account with Hierarchical Namespace (HNS) enabled
async_create = store_client.storage_accounts.begin_create(
    group,
    storage_name,
    {
        'location': region,
        'sku': {'name': 'Standard_LRS'},
        'kind': 'StorageV2',
        'is_hns_enabled': True
    }
)
account = async_create.result()
print(f"Successfully created storage account: {account.name}")
