import boto3
from Lib.misc import custom_log

custom_log("Configuring S3 to SNS topic", "DEBUG")
def configure_s3_to_sns(original_bucket_name, topic_arn):
    s3 = boto3.resource('s3')
    bucket_notification = s3.BucketNotification(original_bucket_name)
    custom_log("Cofiguring bucket notification on put method", "DEBUG")
    response = bucket_notification.put(
        NotificationConfiguration={
            'TopicConfigurations': [
                {
                    'TopicArn': topic_arn,
                    'Events': ['s3:ObjectCreated:Put']

                }
            ]
        }
    )
    custom_log(response, "DEBUG")
    # print(response)