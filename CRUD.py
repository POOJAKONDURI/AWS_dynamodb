import boto3

# # Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  

# # Create a table
# table_name = 'Students'
# table = dynamodb.create_table(
#     TableName=table_name,
#     KeySchema=[
#         {
#             'AttributeName': 'StudentID',
#             'KeyType': 'HASH'  # Partition key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'StudentID',
#             'AttributeType': 'S'
#         }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# print(f"Creating table {table_name}...")
# table.wait_until_exists()
# print("Table created successfully.")


table = dynamodb.Table('Students')

# Add a new student
# response = table.put_item(
#     Item={
#         'StudentID': '12345',
#         'Name': 'Alice',
#         'Age': 21,
#         'Course': 'Computer Science'
#     }
# )
# print("Added item:", response)


#

#Update (Modify an Item)
# response = table.update_item(
#     Key={
#         'StudentID': '12345'
#     },
#     UpdateExpression="set Age = :age",
#     ExpressionAttributeValues={
#         ':age': 22
#     },
#     ReturnValues="UPDATED_NEW"
# )
# print("Updated item:", response)


#delete 
response = table.delete_item(
    Key={
        'StudentID': '12345'
    }
)
print("Deleted item:", response)
