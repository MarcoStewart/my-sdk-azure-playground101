#from azure.storage.blob import BlobServiceClient
#import os

#account_name = os.environ.get("ACCOUNT_NAME")
#account_key = os.environ.get("ACCOUNT_KEY")

#print(account_name)
#print(account_key)

from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=mysdk101;AccountKey=0dMTxiGRtHvNAQdZ9tCteTzV6klIKANOzcag0mVHsuwnVKZomy+cDagN40+dp1xc3RnLyIejvXUd+ASt6upcRg==;EndpointSuffix=core.windows.net"
blob_service = BlobServiceClient.from_connection_string(conn_str=connection_string)

print(blob_service)

def list_blobs_flat(self, blob_service_client: BlobServiceClient, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print(f' -> {blob.name}')
