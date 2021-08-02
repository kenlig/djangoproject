from . import views
from django.urls import path

app_name='productsApp'

urlpatterns=[
    path('products/<str:productName>/',views.products,name='products'),
]