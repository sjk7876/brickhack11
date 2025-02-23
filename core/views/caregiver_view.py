from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from core.openaishit.CategorizeWords import catoregizeWordList
from ..models import Node
catagories = ["Choose your Catagories"]

def home(request):
    return render(request, "caretaker/caretakerHome.html",{"objects":catagories})

def upload(request):
    if request.method == "POST":
        print(request.POST)
        uploaded_file = request.FILES['myFile']
        uploaded_name = request.POST.get('myName')
        catagories.append(request.POST.get('newObject'))
        Node.objects.create(name= uploaded_name,image = uploaded_file)
    return HttpResponse("good")

def render_word_list_input_box(request):
    return render(request, "caretaker/caretakerWordListUpload.html", {"objects":catagories})

def render_individual_item_input_box(request):
    nodes = Node.objects.filter(parent=None)
    return render(request, "caretaker/caretakerUploadIndividualItems.html", {"nodes":nodes})

def generate_objects_from_word_list(request):
    if request.method == "POST":
        print(request.POST)
        word_list = request.POST.get('wordList')
        words_in_json = catoregizeWordList(word_list)
    return HttpResponse(words_in_json)

def newCat(request):
    if request.method == "POST":
        print(request.POST)
        catagories.append(request.POST.get('newObject'))
    return render(request,"caretaker/caretakerHome.html",{"objects":catagories})