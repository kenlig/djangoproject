from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def company(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)

def industry(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)
def notice(request):
    html='<html><body><h1>test</h1></body></html>'
    return HttpResponse(html)