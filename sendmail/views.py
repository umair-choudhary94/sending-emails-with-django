from django.http import HttpResponse

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    name = "John"
    subject = 'welcome to  Codevision'
    message = f'Hi {name}, thank you for Contacting-----A company owend by umair choudhary'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["reciever email"]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Email has been sent")
