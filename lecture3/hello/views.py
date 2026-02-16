from django.http import HttpResponse # must be imported to use HttpResponse class in the view function
from django.shortcuts import render
import datetime
# Create your views here.
def index(request): #takes a request argument "an http request object""
    #return HttpResponse("Hello") #HttpResponse is a special class created by Django that takes a string and returns an HTTP response object that can be sent back to the client. in this case, we are returning a simple string "Hello World" as the response. when we visit the URL associated with this view, we will see "Hello World" displayed in the browser.
    return render(request, "hello/index.html.old") #render is a shortcut function provided by Django that combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text. in this case, we are rendering the template "hello/index.html.old" and returning it as the response. when we visit the URL associated with this view, we will see the content of the index.html.old template displayed in the browser.

def brian(request):
    return HttpResponse("Hello, Brian")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
   # return HttpResponse(f"Hello, {name.capitalize()}!") #formated string and it uses the name variable to create a personalized greeting. when we visit the URL associated with this view and provide a name as a parameter, we will see a greeting message that includes the name we provided.
    return render(request, "hello/greet.html", {
        "name": name.capitalize() #this is a python type dict that contains the var name and its value, name.capitalize().
    })

