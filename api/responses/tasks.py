from api.celery import app
from services.mailer import ResponseNotifyService


@app.task
def send_notify_response(serializer, response_to):
    ResponseNotifyService(serializer=serializer, response_to=response_to).send()
