import unittest
import boto3
from moto import mock_dynamodb2
from app import lambda_handler
import json 

@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        """
        Create database resource and mock table
        """
        self.table_name = 'trial-visitor-count'
        self.dynamodb = boto3.resource('dynamodb', 'us-east-1')
        self.table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'identity',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'Visits',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                'AttributeName': 'identity',
                'AttributeType': 'S'
                },
                {
                'AttributeName': 'Visits',
                'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        self.table.wait_until_exists()

        self.table.put_item(
            Item={
                'identity': 'website',
                'Visits': 1
            }
        )    
    
    def test_table_exists(self):
        """
        Test if our mock table is ready
        """
        self.assertIn('trial-visitor-count', self.table.name)
        self.assertEqual(self.table.item_count, 1) 

if __name__ == '__main__':
    unittest.main()