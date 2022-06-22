# Azure import
This repository contains Python code to upload local files to existing Azure Blob storage and Data Lake storage.<br/>
It assumes you already have an Azure subscription and storage account.

You can find resources about it here :

- https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal<br/>
- https://docs.microsoft.com/fr-fr/azure/developer/python/sdk/examples/azure-sdk-example-storage?tabs=cmd<br/>
- https://docs.microsoft.com/fr-fr/azure/developer/python/sdk/examples/azure-sdk-example-storage-use?tabs=cmd<br/>
<br/>

Authentification is made using your connection string, you can find it in the "Access keys" tab of you Storage account.<br/>
Connection string can be inputed raw (not recommended) or using an environment variable.
1. Open a Powershell prompt to add your connection string to environment variables as follows :
```
$Env: AZURE_STORAGE_CONNECTION_STRING = "your connection string"
```
2. You can then input it in the code using :
```
conn_string = ['AZURE_STORAGE_CONNECTION_STRING']
```

### 1. to_blob.py
This script takes local data as input whether it is files, directories with subdir and files and upload it with the same structure in your Blob storage container.<br/>

You need to provide :
  - container_name : the Blob storage container your uploading data to, if doesn't exist it will be created.<br/>
  - local_dir : the path to the local files or directory to upload.

### 2. to_datalake.py
Coming soon
