#firstapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')
    #return HttpResponse('<html><title>To-Do lists</title></html>')
