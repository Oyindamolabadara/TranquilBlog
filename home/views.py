from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm


def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')


def contact(request):
    """ A view to render the contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Website Inquiry'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
                }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, """ Your message has been sent.
            We will contact you as soon as possible.""")
            return redirect('/')

    form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})
