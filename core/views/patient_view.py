from django.shortcuts import render
from ..models import Node

def render_nodes(request):
    # categories = Node.objects.all()
    categories = ['Category 1', 'Category 2', 'Category 3']
    return render(request, "nodes.html", {"nodes": categories})