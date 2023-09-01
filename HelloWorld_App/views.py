from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sayHello(request):
    return HttpResponse('<center><h1 style="color:red">Hello World! Welcome To Learn Django </h1></center>')

