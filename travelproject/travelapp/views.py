from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from . models import place
from . models import member

def demo(request):
    obj=place.objects.all()
    memb=member.objects.all()
    return render(request,"index.html",{'result':obj,'people':memb})

