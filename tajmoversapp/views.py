import datetime

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy

from .forms import ContactForm

# Create your views here.

def homepage(request):
    todays_date = datetime.datetime.now()
    return render(request, 'index.html',{'todays_date':todays_date})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject, message,from_email, ['jmunyiwamwangi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Please input correct details as directed')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            user_name = form.cleaned_data['user_name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            try:
                send_mail(description, user_name,subject, from_email ['jmunyiwamwangi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Please input correct details as directed')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message. We will reply shortly,')
