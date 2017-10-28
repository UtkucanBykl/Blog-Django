from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
@shared_task()
def send_email(subject, message, from_email):
    from_mail = settings.EMAIL_HOST_USER
    to_list = [from_email, settings.EMAIL_HOST_USER]

    send_mail(subject, message, from_mail, to_list, fail_silently=False)