from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from ..models import Node
catagories = ["Choose your Catagories"]

def home(request):
    # return render(request, "caretaker/caretakerHome.html",{"objects":catagories})
    return render(request, "caretaker/caretakerWordListUpload.html", {"objects":catagories})

def upload(request):
    if request.method == "POST":
        print(request.POST)
        uploaded_file = request.FILES['myFile']
        uploaded_name = request.POST.get('myName')
        catagories.append(request.POST.get('newObject'))
        Node.objects.create(name= uploaded_name,image = uploaded_file)
    return HttpResponse("good")

def newCat(request):
    if request.method == "POST":
        print(request.POST)
        catagories.append(request.POST.get('newObject'))
    return render(request,"caretaker/caretakerHome.html",{"objects":catagories})