from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('client_list/', views.client_list, name='client_list'),
    path('order_list/', views.order_list, name='order_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('create_fake/', views.create_fake, name='create_fake'),
    path('order_client/<int:pk>', views.order_client, name='order_client'),
    path('generate_orders/', views.generate_orders, name='generate_orders'),
    path('product_form/', views.product_form, name='product_form'),
]
