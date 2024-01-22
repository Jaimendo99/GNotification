import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv()

load_dotenv(env_path)

RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")

AWS_LAMBDA_FUNCTION_NAME = os.getenv("AWS_LAMBDA_FUNCTION_NAME")
AWS_LAMBDA_REGION = os.getenv("AWS_LAMBDA_REGION")
AWS_API_ID = os.getenv("AWS_API_ID")
AWS_API_STAGE = os.getenv("AWS_API_STAGE")
