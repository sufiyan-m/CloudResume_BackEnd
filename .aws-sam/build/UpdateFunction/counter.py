import json
import boto3 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CounterUp')


def lambda_handler(event, context):
    response = table.update_item(
        Key = {"id": "msufiyan.com"},
        ExpressionAttributeNames = {'#C': "Visits"},
        UpdateExpression = "SET #C = #C + :val",
        ExpressionAttributeValues = {":val": 1},
        ReturnValues = "UPDATED_NEW"
    )
    number_of_visits = response['Attributes']['Visits']
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": number_of_visits
    }
