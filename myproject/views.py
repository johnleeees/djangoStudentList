#2.create home  Function
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
#4.now we want to link the message , so it can be pass on through the templates- so we create templates folder and files as on the right
#so we change it from return HttpResponse('Hello world!') to render (request,'home.html')
#also need to go to settings.py and register the templates
#also import render function
