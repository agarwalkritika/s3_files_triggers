import boto3
import json
from Lib import misc
import time

def create_role():
    assume_role_string = json.dumps({
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "lambda.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    })

    client = boto3.client('iam')
    random_string = misc.create_random_string(4)
    role_name = 'Lambda_execution_and_S3_full_permissions1'+ str(random_string)
    response1 = client.create_role(
        RoleName= role_name,
        AssumeRolePolicyDocument=assume_role_string
    )

    policy_s3 = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
    policy_lambda_execution = 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'

    response2 = client.attach_role_policy(
        RoleName=role_name, PolicyArn= policy_s3)

    response3 = client.attach_role_policy(
        RoleName = role_name, PolicyArn =policy_lambda_execution
    )
    time.sleep(10)
    return response1['Role']['Arn']