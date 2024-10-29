import boto3

# # Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 

import csv

table = dynamodb.Table('Students')
response = table.scan()
items = response['Items']

with open('C:/Users/pooja konduri/OneDrive/Desktop/BridgeLabs/exported_students.csv', 'w', newline='') as csvfile:
    fieldnames = ['StudentID', 'Name', 'Age', 'Course']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in items:
        writer.writerow(item)

print("Data exported successfully.")
