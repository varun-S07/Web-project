from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request,'login.html') 
    
def donation(request):
    return render(request,'donation.html')