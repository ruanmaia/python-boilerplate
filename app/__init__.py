#### LIBRARIES IMPORT
import os
import logging
import yaml
import boto3

from decimal import getcontext

#### BASIC APP CONFIGURATIONS
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
APP_VERSION = '1.0.0'

with open(BASE_PATH + '/../config.yml') as r:
    config = yaml.safe_load(r.read())

#### WEB APPLICATION
from flask import Flask

app = Flask(__name__)
app.config.update(**config)

#### AWS/S3 Configuration
s3 = boto3.client(
    's3',
    aws_access_key_id=app.config['AWS']['S3']['ACCESS_KEY'],
    aws_secret_access_key=app.config['AWS']['S3']['SECRET_KEY']
)

#### AWS/SES Configuration
ses = boto3.client(
    'ses',
    aws_access_key_id=app.config['AWS']['SES']['ACCESS_KEY'],
    aws_secret_access_key=app.config['AWS']['SES']['SECRET_KEY']
)

#### LOG CONFIGURATION
from loguru import logger
logger.add(BASE_PATH + '/../logs/app.log', retention='6 hours')

#### CELERY CONFIGURATION
from celery import Celery
queue = Celery('tasks', broker='redis://localhost')

from app.tasks import *