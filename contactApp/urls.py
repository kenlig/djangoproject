from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name='contactApp'

URLPattern=[
    path('contact/',views.contact,name='contact'),
    path('recruit/',views.recruit,name='recruit'),
]