from django.shortcuts import render
from .models import Consumerprofile

# Create your views here.

def conprofile(request):
    profile = Consumerprofile.objects.all()
    print(profile)
    return render(request,'consumer/conprofile.html',{'profile':profile})
