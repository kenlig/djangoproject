from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)

def recruit(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)