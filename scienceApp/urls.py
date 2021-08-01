from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name='scienceApp'

URLPattern=[
    path('science/',views.science,name='science'),
]