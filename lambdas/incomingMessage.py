import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    print("EVENT:")
    print(event)
    record = event['Records'][0]['dynamodb']['NewImage']
    print("RECORD:")
    print(record)
    
    sender = record['sender']['S']
    recipient = record['recipient']['S']
    
    if (sender == 'Michael'):
        try:
            date = record['date']['S']
            msgId = record['msgId']['S']
            
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
            messages = dynamodb.Table('messagebody')
            query = messages.query(
                KeyConditionExpression = Key('msgId').eq(msgId)            
            )
            messageBody = query['Items']
            print(messageBody[0]['msgBody'])
            
            email = 'To ' + sender +'\n' + \
                    'From: ' + recipient + '\n' + \
                    'Date: ' + date + '\n' + \
                    'Subject: ' + recipient + '\n' + \
                    'Message: ' + messageBody[0]['msgBody']
            print('EMAIL:')
            print(email)
            key = str(date)+'_'+str(recipient)+'.txt'
            s3 = boto3.client('s3')
            s3.put_object(Body=email, Bucket='videolecture-demo-michael-outbox', Key=key)
            return email
    
        except Exception as e:
            print(e)
            return 0


    if (recipient == 'Michael'):
        try:
            date = record['date']['S']
            msgId = record['msgId']['S']
            
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
            messages = dynamodb.Table('messagebody')
            query = messages.query(
                KeyConditionExpression = Key('msgId').eq(msgId)            
            )
            messageBody = query['Items']
            print(messageBody[0]['msgBody'])
            
            email = 'To ' + sender +'\n' + \
                    'From: ' + recipient + '\n' + \
                    'Date: ' + date + '\n' + \
                    'Subject: ' + recipient + '\n' + \
                    'Message: ' + messageBody[0]['msgBody']
            print('EMAIL:')
            print(email)
            key = str(date)+'_'+str(sender)+'.txt'
            s3 = boto3.client('s3')
            s3.put_object(Body=email, Bucket='videolecture-demo-michael-inbox', Key=key)
            return email
            
        except Exception as e:
            print(e)
            return 0
