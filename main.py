from RabbitMQ import RabbitMQ
import logging
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

logger = logging.getLogger(__name__)


class Notification(BaseModel):
    title: str
    body: str


@app.post("/notification")
async def notification(message: Notification):
    channel = RabbitMQ().get_channel()
    send_notification(json.dumps(dict(message)), channel)
    return {"message": "Notification sent successfully"}


def send_notification(message, channel):
    try:
        channel.basic_publish(exchange='g_notifications', routing_key='', body=message)
        logger.info('Notification sent to RabbitMQ with the message: {}'.format(message))
    except Exception as e:
        print(e)