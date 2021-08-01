from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name='serviceApp'

URLPattern=[
    path('download/',views.download,name='download'),
    path('platform/',views.platform,name='platform'),
]