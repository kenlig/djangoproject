from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    html='<html><body>首页</body></html>'
    return HttpResponse(html)