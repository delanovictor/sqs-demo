# sqs-demo

## Setup

### Instalar SDK da AWS (boto3)

```sh
python -m venv ./.venv/

source ./.venv/bin/activate

pip install boto3
```

### Autenticação

1. Instalar aws-cli; https://awscli.amazonaws.com/AWSCLIV2.msi

2. Configurar credencial

```sh
aws configure

AWS Access Key ID: \\<ACCESS_KEY\\>
AWS Secret Access Key: \\<SECRET_KEY\\> 
Default region name: sa-east-1
```


### Testar Demo 

cd demo-1

```sh
python publish.py

python receive.py
```
