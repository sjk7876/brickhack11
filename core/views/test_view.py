from django.shortcuts import render, HttpResponse
from ..models import Node

def home(request):
    node = Node.objects.get(id=3)
    return render(request, "home.html", {"node" : node})