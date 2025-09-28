from django.http import 
from django.shortcuts import render
from base.models import Person
# Create your views here.

def home(request):
    per = Person.objects.all()
    context = {
        "per" : per,
    }
    return render(request, "home.html", context)

def about(request):
    return HttpRespons("About page")