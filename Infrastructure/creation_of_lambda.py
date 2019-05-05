import boto3
import os
from Lib import misc

misc.custom_log("Making Zip file for lambda code", "DEBUG")
zip_file_path = os.path.join("Lambda_Code", "lambda_code.zip")
if not (os.path.exists(zip_file_path)):
    print("Lambda file location => {}".format(zip_file_path))
    raise misc.Custom_Exception("Lambda Code file does not exist !!")
# print(zip_file_path)
# with open(zip_file_path, 'rb') as fp:
#     print (fp)
misc.custom_log("Zip file successfully created", "DEBUG")
misc.custom_log("Creating Lambda", "DEBUG")
def create_lambda(destination_name, role_arn):
    lambda_client = boto3.client('lambda')
    misc.custom_log("Opening zip file for lambda code", "DEBUG")
    with open(zip_file_path, 'rb') as f:
        zipped_code = f.read()
    random_string = misc.create_random_string(4)
    function_name = 'Automatic_backup_creator'+str(random_string)
    response = lambda_client.create_function(
        FunctionName= function_name,
        Environment={
            'Variables': {
                'dest_bucket_name': destination_name
            }
        },
        Runtime='python3.6',
        Role=role_arn,
        Handler='lambda_handler.lambda_handler',
        Code={
            'ZipFile':zipped_code
        },
        Description='Creates backup of your S3 bucket which you have given whenever a new file has been uploaded to it'
    )
    misc.custom_log("Checking for Return code", "DEBUG")
    if not(response['ResponseMetadata']['HTTPStatusCode'] >= 200 and response['ResponseMetadata']['HTTPStatusCode'] <= 299):
        raise misc.Custom_Exception("Lambda creation failed")
    response_add_permissions = lambda_client.add_permission(
        FunctionName=function_name,
        StatementId='sns_invoke_1567890',
        Action='lambda:InvokeFunction',
        Principal="sns.amazonaws.com"
    )
    misc.custom_log(response, "DEBUG")
    return response['FunctionArn']