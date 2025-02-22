from django.shortcuts import render, HttpResponse
from ..models import Node
from ..DTOs.NodeDTO import load_nodes_from_json

def render_nodes(request, node_id=None):
    # categories = Node.objects.all()
    nodes = load_nodes_from_json()
    return render(request, "nodes.html", {"nodes": nodes})

def print_something(request, node_id):
    print("OSAHFDLASDF " + node_id)
    return HttpResponse("Hello, world. You're at the polls index.")