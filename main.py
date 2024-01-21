import ENV_VAR
import pika
import logging


RABBITMQ_USERNAME = ENV_VAR.RABBITMQ_USERNAME
RABBITMQ_PASSWORD = ENV_VAR.RABBITMQ_PASSWORD

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.100.141', credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='g_notifications', exchange_type='fanout')
    logger.info('Connection to RabbitMQ successful')
except Exception as e:
    print(e)

def send_notification(message):
    try:
        channel.basic_publish(exchange='g_notifications', routing_key='', body=message)
        logger.info('Notification sent to RabbitMQ with the message: {}'.format(message))
        
    except Exception as e:
        print(e)


send_notification('Hello World!')
