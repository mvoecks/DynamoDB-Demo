# Information and code gathered from:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
import boto3

dynamodb = boto3.resource("dynamodb", region_name='us-west-2')

print("Creating messages table")
messages = dynamodb.create_table(
    TableName='messages',
    KeySchema = [
        {
            'AttributeName': 'recipient',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'date',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'recipient',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'date',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
messages.meta.client.get_waiter('table_exists').wait(TableName='messages')

print("Messages table created")

print("Creating message body table")
messagebody = dynamodb.create_table(
    TableName='messagebody',
    KeySchema = [
        {
            'AttributeName': 'msgId',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'msgId',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
messages.meta.client.get_waiter('table_exists').wait(TableName='messages')

print("Message body table created")


