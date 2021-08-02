from . import views
from django.urls import path

app_name='scienceApp'

urlpatterns=[
    path('science/',views.science,name='science'),
]