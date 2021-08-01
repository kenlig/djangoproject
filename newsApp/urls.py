from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name='newsApp'

URLPattern=[
    path('company/',views.company,name='company'),
    path('industry/',views.industry,name='industry'),
    path('notice/',views.notice,name='notice'),
]