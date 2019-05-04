import boto3
import json
from Lib import misc


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

    output_get = sns.get_topic_attributes(
        TopicArn=response['TopicArn']
    )

    attribute_policy_dict =json.loads(output_get['Attributes']['Policy'])
    attribute_name_string = json.dumps(output_get['Attributes'])
    # print(attribute_policy_dict)
    attribute_policy_dict['Statement'][0].pop('Condition', None)
    attribute_policy_string = json.dumps(attribute_policy_dict)
    # print(attribute_policy_string)
    output_set = sns.set_topic_attributes(
        TopicArn=response['TopicArn'],
        AttributeName='Policy',
        AttributeValue=attribute_policy_string
    )
    if not(response['ResponseMetadata']['HTTPStatusCode'] >= 200 and response['ResponseMetadata']['HTTPStatusCode'] <= 299):
        raise misc.Custom_Exception("SNS topic creation failed")
    return response['TopicArn']

