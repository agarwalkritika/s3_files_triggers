import boto3

def configure_s3_to_sns(original_bucket_name, topic_arn):
    s3 = boto3.resource('s3')
    bucket_notification = s3.BucketNotification(original_bucket_name)
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

    # print(response)