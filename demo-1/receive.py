import boto3
import json
from datetime import date
import time

sqs = boto3.client('sqs')

queue_url = 'https://sqs.sa-east-1.amazonaws.com/865522842129/demo-queue-1'

while True:
    print()
    print('Pooling...')

    response = sqs.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages=2, # Lê no máximo 2 mensagens da fila
        VisibilityTimeout=5,
        WaitTimeSeconds=10  # Espera até 10 segundos por uma mensagem
    )
    
    if 'Messages' not in response:
        print('Nenhuma mensagem encontrada...')
        continue
    
    print('Mensagens Consumidas: ', len(response['Messages']))
    
    for message in response['Messages']:
        
        print()
        print('messageId: ', message['MessageId'])
        print(message['Body'])
        
        # Faz algo com a mensagem
        time.sleep(2)
        
        
        sqs.delete_message(
            QueueUrl = queue_url,
            ReceiptHandle = message['ReceiptHandle']
        )
        
        print('Mensagem Excluída!')
        
        
        