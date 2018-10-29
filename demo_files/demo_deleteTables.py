import boto3

dynamodb = boto3.resource("dynamodb", region_name='us-east-1')

print("Deleting the messages table")
messages = dynamodb.Table('messages')
messages.delete()
messages.meta.client.get_waiter('table_not_exists').wait(TableName='messages')

print("Deleting the message body table")
messageBodys = dynamodb.Table('messagebody')
messageBodys.delete()
messages.meta.client.get_waiter('table_not_exists').wait(TableName='messagebody')
