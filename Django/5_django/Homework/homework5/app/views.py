from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from .models import Product


# Create your views here.
def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            product = Product.objects.create(name=name, description=description, price=price, count=count, image=image)
            product.save()
            return HttpResponse('ok')

    else:
        form = ProductForm()

    return render(request, 'app/product_form.html', {'form': form})
