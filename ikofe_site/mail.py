from django.core.mail import send_mail

SERVER_MAIL = ''


def create_and_send_mail(recipient, subj, text):
    send_mail(subj, text, SERVER_MAIL, [recipient], fail_silently=False)