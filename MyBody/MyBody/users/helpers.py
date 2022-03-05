import os

from django.core.mail import EmailMessage


def send_email_message(email, username=None):
    body = f'Thank you for your registration!\nYou are welcome!!'
    sender = os.environ.get('GMAIL_USER')
    header = 'Hello, Best Regards!'

    if username:
        body = f'Thank you for your registration {username}!\nYou are welcome!!' \
               f'\nNow you can create articles, edit and delete them.'

    email = EmailMessage(
        header,
        body,
        sender,
        [email],
    )

    email.send(fail_silently=False)
