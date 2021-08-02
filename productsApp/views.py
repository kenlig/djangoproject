from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def products(request,productName):
    submenu=productName
    if productName == 'robot':
        productName='家用机器人'
    elif productName == 'monitor':
        productName='智能监控'
    else:
        productName='人脸识别解决方案'

    return render(request,'productList.html',{'active_menu':'products','sub_menu':submenu,'productName':productName})