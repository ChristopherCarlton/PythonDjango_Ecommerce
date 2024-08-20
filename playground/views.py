from django.shortcuts import render
from django.db.models import Q, F, Func, Value
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Customer, Collection

def say_hello(request):
    collection = Collection(pk=11)
    collection.title = 'Games'
    collection.featured_product = None
    collection.save()




    return render(request, 'hello.html', {'name': 'Mosh'})
