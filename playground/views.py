# from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
# from templated_mail.mail import BaseEmailMessage
from django.shortcuts import render
from .tasks import notify_customers

# sending an email
# def say_hello(request):
#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name': 'Mosh'}
#         )
#         message.send(['john@moshbuy.com'])
#     except BadHeaderError:
#         pass 
#     return render(request, 'hello.html', {'name': 'Mosh'})

def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Mosh'})
