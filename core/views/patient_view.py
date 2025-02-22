from django.shortcuts import render
from ..models import Node
from ..DTOs.NodeDTO import load_nodes_from_json

def render_nodes(request):
    # categories = Node.objects.all()
    nodes = load_nodes_from_json()
    return render(request, "nodes.html", {"nodes": nodes})