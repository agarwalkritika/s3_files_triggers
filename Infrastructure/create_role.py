import boto3
import json
from Lib import misc
import time

misc.custom_log("Creatin custom role for lambda", "DEBUG")
def create_role():
    misc.custom_log("Assume role policy document", "DEBUG")
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
    misc.custom_log("Generating random string for role name", "DEBUG")
    random_string = misc.create_random_string(4)
    misc.custom_log("Initialising role name", "DEBUG")
    role_name = 'Lambda_execution_and_S3_full_permissions1'+ str(random_string)
    misc.custom_log("Now trying to create role", "DEBUG")
    response1 = client.create_role(
        RoleName= role_name,
        AssumeRolePolicyDocument=assume_role_string
    )
    misc.custom_log("S3 full access Policy arn", "DEBUG")
    policy_s3 = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
    misc.custom_log("Lambda basic execution role policy arn", "DEBUG")
    policy_lambda_execution = 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    misc.custom_log("Attaching S3 full access policy to role", "DEBUG")
    response2 = client.attach_role_policy(
        RoleName=role_name, PolicyArn= policy_s3)
    misc.custom_log("Attaching Lambda basic execution role policy to Role ", "DEBUG")
    response3 = client.attach_role_policy(
        RoleName = role_name, PolicyArn =policy_lambda_execution
    )
    misc.custom_log("Now sleeping for 10 seconds to ensure IAM role is created successfully", "DEBUG")
    time.sleep(10)
    misc.custom_log("Returning Newly created Role's arn", "DEBUG")
    misc.custom_log( response1, "DEBUG")
    return response1['Role']['Arn']
