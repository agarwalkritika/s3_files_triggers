import boto3


def configure_sns_to_lambda(topic_arn, function_arn):
    client = boto3.client('sns')
    response = client.subscribe(
        TopicArn=topic_arn,
        Protocol='lambda',
        Endpoint=function_arn,
        ReturnSubscriptionArn=True
    )

    # print(response)