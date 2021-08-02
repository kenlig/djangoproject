from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def science(request):
    return render(request,'science.html',{'active_menu':'science',})