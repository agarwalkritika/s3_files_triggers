import boto3
import random
from Lib import misc

misc.custom_log("Creating S3 bucket for backup", "DEBUG")
def create_s3_backup_file():
        random_string = misc.create_random_string(4)
        s3 = boto3.client('s3')
        response = s3.create_bucket( Bucket = 'backupfiles' + str(random_string))
        misc.custom_log("Checking for Return code", "DEBUG")
        if not(response['ResponseMetadata']['HTTPStatusCode'] >= 200  and response['ResponseMetadata']['HTTPStatusCode'] <= 299):
                print(response)
                raise misc.Custom_Exception("S3 bucket creation failed")
        location = response['Location']
        bucket_name = location[1:]
        misc.custom_log(response, "DEBUG")
        return bucket_name

