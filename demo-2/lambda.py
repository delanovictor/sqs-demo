import boto3
import cv2
import numpy as np

s3 = boto3.client('s3')
TARGET_BUCKET = 'demo-delano-unisinos-2024-destino'

def lambda_handler(event, context):
    for record in event['Records']:

        bucket = record['s3']['bucket']['name'] # demo-delano-unisinos-2024
        key = record['s3']['object']['key']     # cat.jpg
        
        convert_image(bucket, key)
        
def convert_image(bucket, key):
    # Pega imagem no S3
    get_object_response = s3.get_object(
        Bucket=bucket, 
        Key=key
    )
    # Converte imagem para cinza   
    img_bytes = get_object_response['Body'].read()
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Salva imagem no bucket S3 de destino  
    img_gray_bytes = cv2.imencode('.jpg', img_gray)[1].tobytes()
    s3.put_object(Bucket=TARGET_BUCKET,  Key =f"gray-${key}", Body=img_gray_bytes)
    
    