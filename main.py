from Infrastructure import *
from Lib.misc import custom_log

# Required Original bucket name from where to copy the new uploaded file
custom_log("Reqesting for bucket name")
original_bucket_name = input("Enter bucket name")
custom_log("Received bucket name "+str(original_bucket_name))

custom_log("Now creating custom role")
role_arn = create_role.create_role()
custom_log("Custom role has been created")

custom_log("Now creating S3 backup bucket ")
bucket_name = creation_of_S3_bucket.create_s3_backup_file()
custom_log("Backup bucket has been successfully created")

custom_log("Creating Lambda function and attaching role to it")
function_arn =creation_of_lambda.create_lambda(bucket_name, role_arn)
custom_log("Lambda function successfully created")

custom_log("Creating SNS Topic")
topic_arn = creation_of_SNS_Topic.create_sns()
custom_log("SNS topic has been created")

custom_log("Configuring Original S3 bucket with SNS topic")
configure_origS3_to_SNS_topic.configure_s3_to_sns(original_bucket_name,topic_arn)
custom_log("Configuration of S3 to SNS successfull")

custom_log("Configuring SNS to Lambda function")
configure_sns_to_lambda.configure_sns_to_lambda(topic_arn,function_arn)
custom_log("Successfull configured SNS to Lambda")