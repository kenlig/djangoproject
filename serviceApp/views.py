from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def download(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)
def platform(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)