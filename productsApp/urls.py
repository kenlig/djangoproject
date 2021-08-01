from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name='productApp'

URLPattern=[
    path('robot/',views.robot,name='robot'),
    path('monitoring/',views.monitoring,name='monitoring'),
    path('face/',views.face,name='face'),
]