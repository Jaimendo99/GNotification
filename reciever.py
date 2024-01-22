import json
from RabbitMQ import RabbitMQ
import requests
import logging
from ENV_VAR import AWS_LAMBDA_FUNCTION_NAME, AWS_LAMBDA_REGION, AWS_API_ID, AWS_API_STAGE

logger = logging.getLogger(__name__)

channel = RabbitMQ().get_channel()

result = channel.queue_declare(queue='g_notifications', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='g_notifications', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def send_notification_lambda(title: str, body: str):
    url = f'https://{AWS_API_ID}.execute-api.{AWS_LAMBDA_REGION}.amazonaws.com/{AWS_API_STAGE}/{AWS_LAMBDA_FUNCTION_NAME}'
    json = {
        "title": title,
        "body": body
    }
    return  requests.post(url, json=json)


def callback(ch, method, properties, body):
    data = body.decode('utf-8')
    dataJs = json.loads(data)

    res = send_notification_lambda(dataJs['title'], dataJs['body'])
    print(res,dataJs['title'], dataJs['body'])


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()