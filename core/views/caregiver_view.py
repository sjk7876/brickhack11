from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from core.openaishit.CategorizeWords import catoregizeWordList
from core.openaishit.ExpandWords import expandWord
from core.openaishit.GenerateImage import generateImage
from ..models import Node
catagories = ["Choose your Catagories"]

def home(request):
    return render(request, "caretaker/caretakerPageLayout.html",{"objects":catagories})

def render_Generate(request):
    nodes = Node.objects.filter(parent=None)
    return render(request, "caretaker/caretakerGenerate.html", {"nodes":nodes})

def upload(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        category_id = request.POST.get('category_id')
        image = request.FILES.get("image")
        
        parent = Node.objects.get(id=category_id) if category_id else None
        Node.objects.create(name=name, parent=parent, image=image)
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
    return HttpResponse("good")

def generate_single_image(request):
    if request.method == "POST":
        print(request.POST)
        word = request.POST.get('name')
        category_id = request.POST.get('category_id')
        
        parent = Node.objects.get(id=category_id)
        category = parent.name if parent else None
        
        longer_word = expandWord(word, category)
        generateImage(longer_word, category, word)
        filepath = f"core/static/images/{word}.png"
        
        Node.objects.create(name=word, parent=parent, image=filepath)
    return HttpResponse("good")

def newCat(request):
    if request.method == "POST":
        print(request.POST)
        catagories.append(request.POST.get('newObject'))
    return render(request,"caretaker/caretakerHome.html",{"objects":catagories})