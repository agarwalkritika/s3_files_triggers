from Infrastructure import *

original_bucket_name = 'origbucket001'
bucket_name = creation_of_S3_bucket.create_s3_backup_file()
function_arn =creation_of_lambda.create_lambda(bucket_name)
topic_arn = creation_of_SNS_Topic.create_sns()
configure_origS3_to_SNS_topic.configure_s3_to_sns(original_bucket_name,topic_arn)
configure_sns_to_lambda.configure_sns_to_lambda(topic_arn,function_arn)