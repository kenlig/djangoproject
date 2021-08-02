from . import views
from django.urls import path

app_name='newsApp'

urlpatterns=[
    path('company/',views.company,name='company'),
    path('industry/',views.industry,name='industry'),
    path('notice/',views.notice,name='notice'),
]