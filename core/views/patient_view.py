from django.shortcuts import render
from ..models import Node
from ..DTOs.NodeDTO import load_nodes_from_json

NODES = load_nodes_from_json()

def render_nodes(request):
    categories = Node.objects.all()
    return render(request, "nodes.html", {"nodes": categories})

def render_children(request, node_id):
    node = Node.objects.get(id=node_id)
    children = node.children.all()
    return render(request, "nodes.html", {"nodes": children})