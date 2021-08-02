from . import views
from django.urls import path

app_name='contactApp'

urlpatterns=[
    path('contact/',views.contact,name='contact'),
    path('recruit/',views.recruit,name='recruit'),
]