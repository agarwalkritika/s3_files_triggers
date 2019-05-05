import boto3
import json
from Lib import misc

misc.custom_log("Creating SNS topic", "DEBUG")
def create_sns():
    sns = boto3.client('sns')
    random_string = misc.create_random_string(4)
    name = 'NewSNSTopic' + str(random_string)
    response = sns.create_topic(
        Name= name,
        Attributes={
            'DisplayName':'New file is uploaded'
        },
        Tags=[
            {
                'Key': 'SNS to trigger Lambda',
                'Value': 'whenever new file is uploaded_take backup'
            }
        ]
    )
    misc.custom_log("Taking topic arn from SNS topic ", "DEBUG")
    output_get = sns.get_topic_attributes(
        TopicArn=response['TopicArn']
    )

    attribute_policy_dict =json.loads(output_get['Attributes']['Policy'])
    # print(attribute_policy_dict)
    attribute_policy_dict['Statement'][0].pop('Condition', None)
    attribute_policy_string = json.dumps(attribute_policy_dict)
    # print(attribute_policy_string)

    misc.custom_log("Setting attribute's access policy of topic arn ", "DEBUG")
    output_set = sns.set_topic_attributes(
        TopicArn=response['TopicArn'],
        AttributeName='Policy',
        AttributeValue=attribute_policy_string
    )
    if not(response['ResponseMetadata']['HTTPStatusCode'] >= 200 and response['ResponseMetadata']['HTTPStatusCode'] <= 299):
        raise misc.Custom_Exception("SNS topic creation failed")
    misc.custom_log(response, "DEBUG")
    return response['TopicArn']

