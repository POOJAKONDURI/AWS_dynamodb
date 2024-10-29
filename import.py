import boto3

# # Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  

import csv

table = dynamodb.Table('Students')

with open('C:/Users/pooja konduri/OneDrive/Desktop/BridgeLabs/AWS_dynamodb/students.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        table.put_item(Item=row)
print("Data imported successfully.")
