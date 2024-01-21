import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv()

load_dotenv(env_path)

RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
