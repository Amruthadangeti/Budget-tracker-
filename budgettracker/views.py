from django.shortcuts import render
from django.http import HttpResponse
from Goodbudget.models import Envelope
from Honeydue.models import  Project
from pocketGuard.models import Account
from django.contrib.auth.decorators import login_required
 
@login_required 
def index(request):
    return render(request,'index.html')
@login_required
def Goodbudget(request):
    book = Envelope.objects.all()
    return render(request, 'Goodbudget.html' ,{'Envelope': book})
@login_required
def Honeydue(request):
    honey = Project.objects.all()
    return render(request, 'Honeydue.html' ,{' Project': honey})
@login_required
def pocketGuard(request):
    pocket = Account.objects.all()
    return render(request, 'pocketGuard.html' ,{'Account': pocket})