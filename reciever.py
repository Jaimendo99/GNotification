import ENV_VAR
import pika
import logging
import requests

logger = logging.getLogger(__name__)

RABBITMQ_USERNAME = ENV_VAR.RABBITMQ_USERNAME
RABBITMQ_PASSWORD = ENV_VAR.RABBITMQ_PASSWORD


try:
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.100.141', credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='g_notifications', exchange_type='fanout')
    logger.info('Connection to RabbitMQ successful')
except Exception as e:
    print(e)



result = channel.queue_declare(queue='g_notifications', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='g_notifications', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()