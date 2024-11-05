# emailer/utils.py

from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.conf import settings


def send_bulk_email(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )
        return True
    except BadHeaderError:
        return False
