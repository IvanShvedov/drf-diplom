from api.celery import app
from services.mailer import ResponseNotifyService


@app.task(bind=True, default_retry_delay=10 * 60, ignore_result=True)
def send_notify_response(serializer, response_to):
    ResponseNotifyService(serializer=serializer, response_to=response_to).send()
