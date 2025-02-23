from django.shortcuts import render, HttpResponse

def home(request):
    objects = ["Apple","Pinnaple","Blueberry","Tables"]
    return render(request, "caretaker/caretakerHome.html",{"objects":objects})