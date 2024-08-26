# from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
# from templated_mail.mail import BaseEmailMessage
from django.shortcuts import render
# from .tasks import notify_customers
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__) 
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

class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieived the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': data})
