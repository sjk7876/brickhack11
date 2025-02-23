from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from core.openaishit.CategorizeWords import catoregizeWordList
from core.openaishit.ExpandWords import expandWord
from core.openaishit.GenerateImage import generateImage
from ..models import Node
catagories = ["Choose your Catagories"]

def home(request):
    return render(request, "caretaker/caretakerPageLayout.html",{"objects":catagories})

def upload(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        category_id = request.POST.get('category_id')
        image = request.FILES.get("image")
        
        Node.objects.create(name=name, parent=category_id, image=image)
    return HttpResponse("good")

def render_word_list_input_box(request):
    return render(request, "caretaker/caretakerWordListUpload.html", {"objects":catagories})

def render_individual_item_input_box(request):
    nodes = Node.objects.filter(parent=None)
    return render(request, "caretaker/caretakerUploadIndividualItems.html", {"nodes":nodes})

# def generate_objects_from_word_list(request):
#     if request.method == "POST":
#         print(request.POST)
#         word_list = request.POST.get('wordList')
#         words_in_json = catoregizeWordList(word_list)
#     return HttpResponse("good")
def generate_objects_from_word_list(request):
    if request.method == "POST":
        word_list = request.POST.get('wordList')
        words_in_json = catoregizeWordList(word_list)

        # Store generated image paths
        image_paths = []
        for word in words_in_json:
            category = None  # You might want to customize this based on your logic
            longer_word = expandWord(word, category)
            generateImage(longer_word, category, word)
            filepath = f"{settings.STATIC_URL}images/{word}.png"
            
            # Save the image path to be passed to the template
            image_paths.append(filepath)

        # Render the template with the image paths
        return render(request, "caretaker/caretakerDisplayImages.html", {"image_paths": image_paths})

    return HttpResponse("Invalid method", status=405)


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
        
        Node.objects.create(name=word, parent=category, image=filepath)
    return HttpResponse("good")

def newCat(request):
    if request.method == "POST":
        print(request.POST)
        catagories.append(request.POST.get('newObject'))
    return render(request,"caretaker/caretakerHome.html",{"objects":catagories})