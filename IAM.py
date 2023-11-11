import boto3
import os
import configparser
from logging import Logger

def __init__(self, aws_config_file=None):
        if aws_config_file is None:
            aws_config_file = os.getenv('SEAM_AWS_CONFIG', '~/.aws/config')

        try:
            parser = configparser.ConfigParser()
            parser.read(aws_config_file)

            self.aws_config = {
                'default': {
                    'region': parser['default'].get('region', 'us-east-1'),
                    'aws_access_key_id': parser['default'].get('aws_access_key_id'),
                    'aws_secret_access_key': parser['default'].get('aws_secret_access_key'),
                }
            }

            if not self.aws_config['default']['aws_access_key_id'] or not self.aws_config['default']['aws_secret_access_key']:
                raise Exception('Config is empty')

        except Exception as error:
            Logger.info('Cannot read from aws config file: {}'.format(error))
            Logger.info('Try to read from env variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION')

            self.aws_config = {
                'default': {
                    'aws_access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
                    'aws_secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
                    'region': os.getenv('AWS_DEFAULT_REGION', 'us-east-1'),
                }
            }

# Create IAM client
iam = boto3.client('iam')


# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)