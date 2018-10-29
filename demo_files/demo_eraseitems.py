# Thanks github user swalloow for the code
# Link: https://gist.github.com/Swalloow/9966d576a9aafff482eef6b59c222baa

import boto3

dynamodb = boto3.resource('dynamodb', 'us-west-2')
messages = dynamodb.Table('messages')
messageBodys = dynamodb.Table('messagebody')

scanmessages = messages.scan(
    ProjectionExpression='recipient',
)

#scanbodies = messageBodys.scan(
#    ProjectionExpression='msgId',
#)

    for each in scanmessages['Items']:
        print(each)
        break;
        batch.delete_item(Key=each)

#with messageBodys.batch_writer() as batch:
#    for each in scanbodies['Items']:
#        print(each)
#        batch.delete_item(Key=each)
