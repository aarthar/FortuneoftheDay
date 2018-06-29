import boto3

dynamodb_resource = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')
dynamodb_client = boto3.client('dynamodb')

table = dynamodb_resource.Table('Fortune')

table.put_item(
    Item={
        'index': 1,
        'fortune': "You are fortunate.",
    }
)

table.put_item(
    Item={
        'index': 2,
        'fortune': "Confuscious say, man who sit on toilet, high on pot."
    }
)
