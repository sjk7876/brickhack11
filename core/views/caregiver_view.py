from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from ..models import Node

def home(request):
    objects = ["Choose your Object","Apple","Pinnaple","Blueberry","Tables"]
    return render(request, "caretaker/caretakerHome.html",{"objects":objects})

def upload(request):
    if request.method == "POST":
        print(request.POST)
        uploaded_file = request.FILES['myFile']
        Node.objects.create(name="Random",image = uploaded_file)
    return HttpResponse("good")