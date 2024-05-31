from django.shortcuts import render
from django.http import HttpResponse
from Goodbudget.models import Envelope
 
 
def index(request):
    return render(request,'index.html')
def Goodbudget(request):
    book = Envelope.objects.all()
    return render(request, 'Goodbudget.html' ,{'book': book})