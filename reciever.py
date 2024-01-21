from RabbitMQ import RabbitMQ
import logging

logger = logging.getLogger(__name__)

channel = RabbitMQ().get_channel()

result = channel.queue_declare(queue='g_notifications', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='g_notifications', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # TODO: Call the lambda API here
    print(f" [x] {body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()