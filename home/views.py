from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        message_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email_address': email_address,
            'subject': subject,
            'message': message,
        }
        message = '''
            From: {}
            New message: {}
            '''.format(message_data['email_address'], message_data['message'])

        send_mail(
            message_data['subject'], message, '', ['ganiyatbadara@gmail.com'])

        messages.info(request, (
            f'Your message has been sent, we will contact you \
            via { email_address } as soon as possible.'))
        return render(request, 'home/home.html')

    return render(request, 'home/contact.html')