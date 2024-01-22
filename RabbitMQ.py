import pika
import logging
from ENV_VAR import RABBITMQ_PASSWORD, RABBITMQ_USERNAME

logger = logging.getLogger(__name__)

class RabbitMQ:
    def __init__(self):
        self.host = '54.226.251.57'
        self.username = RABBITMQ_USERNAME
        self.password = RABBITMQ_PASSWORD
        
        try:
            credentials = pika.PlainCredentials(self.username, self.password)
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, credentials=credentials))
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange='g_notifications', exchange_type='fanout')
            logger.info('Connection to RabbitMQ successful')
        except Exception as e:
            print('buenoe', e)

    def get_channel(self):
        return self.channel
