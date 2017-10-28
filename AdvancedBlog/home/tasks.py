from celery import shared_task
from django.core.mail import EmailMessage


@shared_task()
def send_email(subject, message, from_email):
    print("utkuuu")
    EmailMessage(subject=subject, body=message, from_email=from_email).send()
