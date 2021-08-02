from . import views
from django.urls import path

app_name='serviceApp'

urlpatterns=[
    path('download/',views.download,name='download'),
    path('platform/',views.platform,name='platform'),
]