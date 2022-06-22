import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


conn_string = # raw connection string or using it through an environment variable
container_name = ""


local_dir = # path/to/data


service_client = BlobServiceClient.from_connection_string(conn_string)
container_client = service_client.get_container_client(container_name)


for subdir, dirs, files in os.walk(local_dir):
    for file in files:

        file_path = os.path.join(subdir, file)

        blob_client = container_client.get_blob_client(file_path)

        with open(file_path, 'r+b') as data:
            blob_client.upload_blob(data)