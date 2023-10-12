from django.http import HttpResponse
from django.shortcuts import render
from .models import Client, Product, Order
from datetime import datetime, timedelta
import random
from django.utils import timezone
from .forms import ProductForm

###############
def main(request):
    return render(request, 'app/main.html')


def about(request):
    return render(request, 'app/about.html')


def create_fake(request):
    for i in range(1, 6):
        Client.objects.create(name=f'Client {i}', email=f'email{i}@example.com', number=f'123456789{i}', address=f'address{i}')

    for i in range(1, 6):
        Product.objects.create(name=f'Product {i}', description=f'description{i}', price=f'{i}', count=i)
    return HttpResponse('OK')
###############


def client_list(request):
    context = {
        'users': Client.objects.all()
    }
    return render(request, 'app/client_list.html', context=context)


def order_list(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'app/order_list.html', context=context)


def product_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'app/product_list.html', context=context)


def order_client(request, pk):
    client = Client.objects.get(pk=pk)
    products = client.order_set.values('product').all()
    if request.method == 'POST':
        date = request.POST.get('date')
        if date == 'day':
            products = products.filter(date_ordered__day=timezone.now().day)
        elif date == 'month':
            products = products.filter(date_ordered__month=timezone.now().month)
        elif date == 'year':
            products = products.filter(date_ordered__year=timezone.now().year)
        else:
            products = products
    context = {
        'pk': pk,
        'products': products,
    }
    return render(request, 'app/order_client.html', context=context)


def generate_orders(request):
    # Определение диапазона значений для id и client_id
    id_range = range(1, 21)
    client_id_range = range(1, 6)

    # Генерация 20 записей
    for _ in range(20):
        order = Order()
        order.id = random.choice(list(id_range))
        order.client_id = random.choice(list(client_id_range))
        order.total_price = random.randint(100, 1000)

        # Генерация случайной даты в последних 365 днях
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=365)
        random_date = datetime.fromordinal(random.randint(start_date.toordinal(), end_date.toordinal()))
        order.date_ordered = random_date

        # Сохранение записи в базе данных
        order.save()

    return HttpResponse('ok')


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            date_added = form.cleaned_data['date_added']
            product = Product()
            product.objects.create(name=name, description=description, price=price, count=count, date_added=date_added)
            product.save()
            return HttpResponse('OK')

    else:
        pass
    return render(request, 'app/product_form.html')
