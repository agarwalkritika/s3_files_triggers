import json
import boto3
import urllib
import os

destination_bucket_name = os.environ.get('dest_bucket_name')

def lambda_handler(event, context):
    message=json.loads(event['Records'][0]['Sns']['Message'])
    # print(message)
    bucket_name =message['Records'][0]['s3']['bucket']['name']
    # print(bucket_name)
    object_key = message['Records'][0]['s3']['object']['key']
    # print(object_key)
    object_key  = urllib.parse.unquote(object_key)
    object_key = object_key.replace('+', ' ')
    # print(object_key)
    s3 = boto3.resource('s3')
    copy_source = {'Bucket': bucket_name,
                            'Key':object_key
                   }
    Destination_bucket = s3.Bucket(destination_bucket_name)
    Destination_bucket.copy(copy_source, 'Dup_through_lambda_SQLNOTES')
