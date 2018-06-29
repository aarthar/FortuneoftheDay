from __future__ import print_function # Python 2/3 compatibility
import boto3
from random import randint
from boto3.dynamodb.conditions import Key, Attr

dynamodb_resource = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb_client = boto3.client('dynamodb')

table_name = 'Fortune'
existing_tables = dynamodb_client.list_tables()['TableNames']

# Check to see if table exists, and create if necessary.
if table_name not in existing_tables:
    print ("Creating table: ", table_name)
    response = dynamodb_resource.create_table(
        TableName='Fortune',
        KeySchema=[
            {
                'AttributeName': 'index',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'fortune',
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'index',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'fortune',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        },
    )
    print("Table status:", table.table_status)

table = dynamodb_resource.Table('Fortune')

# Queries the table and returns the total number of scanned items
def get_index():
    response = table.scan(
        TableName='Fortune',
        Select='COUNT'
    )
    return response['Count']

# Provides a method to load a new fortune into the database
def load_item(fortune):
    new_index = get_index() + 1
    print(new_index)
    table.put_item(
        Item={
            'index': new_index,
            'fortune': fortune
        }
    )

# Gets a random fortune from the database
def get_fortune():
    random = 0
    high = get_index()
    print(high)
    random = randint(1, high)
    response = table.query(
        KeyConditionExpression=Key('index').eq(random)
    )
    return response

print(get_fortune())


#response = table.query(
#    KeyConditionExpression=Key('index')
#)

#for i in response['Items']:
#    print (i['index'], ":", i['fortune'])
