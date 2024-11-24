from fabric.identity import ClientCredential
from fabric.mgmt.resource import ManagementClient
from fabric.mgmt.storage import StorageClient

# Define your Azure subscription details and storage settings
subscription = 'your-subscription-id'
group = 'your-resource-group'
storage_name = 'datalake-storage'
region = 'selected-region'

# Authenticate with Fabric using client credentials
creds = ClientCredential()  # Uses client credentials for authentication
res_client = ManagementClient(creds, subscription)
store_client = StorageClient(creds, subscription)

# Create or update the resource group
res_client.resource_groups.create_or_update(group, {'location': region})

# Create storage account with HNS (Hierarchical Namespace) enabled
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
