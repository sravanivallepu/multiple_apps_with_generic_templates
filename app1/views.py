from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_string(request):
    return HttpResponse('<marquee><h1>app1_string</h1></marquee>')
def app1_page(request):
    return render(request,'app1_page.html') 

from django.http import HttpResponse

def app2_string(request):
    return HttpResponse('<marquee><h1>app2_string</h1></marquee>')
def app2_page(request):
    return render(request,'app2_page.html') 
