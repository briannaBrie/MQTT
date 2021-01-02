#Posting the image in the Azure Blob Storage
from azure.storage.blob import BlockBlobService, PublicAccess
try:
    account_name = os.environ["BLOB_ACCOUNT_NAME"]
except KeyError:
    pass
try:
    account_name = os.environ["BLOB_ACCOUNT_NAME"]
except KeyError:
    pass

def postblob():
    blob_service = BlockBlobService(account_name, account_key)
    container_name = 'webcam'
    #incase you need to create the container
    #blob_service.create_container(container_name)
    #blob_service.set_container_acl 
    #(container_name, public_access=PublicAccess.Container)
    cam.TakePicture()
    blob_service.create_blob_from_path(
        container_name, 
        'picture',
        os.getcwd()+"/home/pi/Desktop/image.jpg"
    )
