from django.shortcuts import render, HttpResponse
from .models import Order, Product, Client
# Create your views here.


def order_list(request):
    orders = Order.objects.all()
    return HttpResponse(orders)


def client_list(request):
    clients = Client.objects.all()
    html = ''
    for client in clients:
        html += f'<p>Имя: {client.name}, Электронный адрес: {client.email}</p>'
    return HttpResponse(html)


def product_list(request):
    products = Product.objects.all()
    return HttpResponse(products)
