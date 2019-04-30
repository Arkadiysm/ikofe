from django.core.mail import send_mail
from iKofe import settings


def create_and_send_mail(recipient, subj, text):
    send_mail(subj, text, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)

