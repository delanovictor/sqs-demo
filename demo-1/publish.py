import boto3
import json
from datetime import datetime

sqs = boto3.client('sqs')

queue_url = 'https://sqs.sa-east-1.amazonaws.com/865522842129/demo-queue-1'

# Publica Mensagem

response = sqs.send_message(
    QueueUrl = queue_url,
    MessageAttributes = {
        'teste-atributo': {
            'DataType': 'String',
            'StringValue': 'abc'
        }
    },
    MessageBody = json.dumps({
        'teste': 123,
        'data': datetime.now().isoformat()
    })
)

print('message_id: ', response['MessageId'])

