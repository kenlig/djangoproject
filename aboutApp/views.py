from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def survey(request):
    return render(request,'survey.html',{'active_menu':'about',})
def honor(request):
    return render(request,'honor.html',{'active_menu':'about',})