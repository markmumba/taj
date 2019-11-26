from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_message(name,reciever,password):
    subject ='message from user'
    sender ='jmunyiwamwangi@gmail.com'

    text_content = render_to_string('email/notification.txt',{"name": name, "password":password})
    html_content = render_to_string('email/notification.html',{"name":name, "password":password})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


