from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def robot(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)
def monitoring(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)
def face(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)