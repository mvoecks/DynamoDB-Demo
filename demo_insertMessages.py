import boto3
import random
import loremipsum

randomSubjects = loremipsum.get_sentences(1000)
contacts = ['David', 'Jason', 'Michael', 'Julian', 'Coleman', 'Adam', 'Julia', 'Mary', 'Eve', 'Samantha']

dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
messages = dynamodb.Table('messages')
messageBodys = dynamodb.Table('messagebody')

for i in range(1):
    # Create a random date
    randomDay = random.randint(1, 28)
    randomMonth = random.randint(1, 12)
    randomYear = random.randint(2000, 2018)
    date = str(randomYear)+"-"+str(randomMonth)+"-"+str(randomDay)

    # Choose Recipient and Sender
    recipient = random.choice(contacts)
    sender = random.choice([x for x in contacts if x != recipient])
    
    messages.put_item(
        Item = {
            'recipient': recipient,
            'date': date,
            'sender': sender,
            'subject': randomSubjects[i],
            'msgId': i
        }
    )
    messageBodys.put_item(
        Item = {
            'msgId': i,
            'msgBody': loremipsum.generate_paragraph()[2]
        }
    )

print("Items in messages table:")
print(messages)
print("Items in message body table:")
print(messageBodys)
