import boto3
from Lib.misc import custom_log

custom_log("Configure SNS to Lambda", "DEBUG")
def configure_sns_to_lambda(topic_arn, function_arn):
    client = boto3.client('sns')
    custom_log("Subscribing lambda to SNS", "DEBUG")
    response = client.subscribe(
        TopicArn=topic_arn,
        Protocol='lambda',
        Endpoint=function_arn,
        ReturnSubscriptionArn=True
    )
    custom_log(response, "DEBUG")
    # print(response)