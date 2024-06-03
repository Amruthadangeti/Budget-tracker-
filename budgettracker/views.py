from django.shortcuts import render
from django.http import HttpResponse
from Goodbudget.models import Envelope
from Honeydue.models import  Project
from pocketGuard.models import Account
 
 
def index(request):
    return render(request,'index.html')
def Goodbudget(request):
    book = Envelope.objects.all()
    return render(request, 'Goodbudget.html' ,{'book': book})
def Honeydue(request):
    book = Project.objects.all()
    return render(request, 'Honeydue.html' ,{'book': book})
def pocketGuard(request):
    book = Account.objects.all()
    return render(request, 'pocketGuard.html' ,{'book': book})