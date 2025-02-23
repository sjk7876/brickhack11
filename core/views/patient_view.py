from django.shortcuts import render
from ..models import Node
from ..DTOs.NodeDTO import load_nodes_from_json

NODES = load_nodes_from_json()

def render_nodes(request, node_id=None):
    if node_id is None:
        nodes = Node.objects.filter(parent=None)
    else:
        parent = Node.objects.get(id=node_id)
        nodes = parent.children.all()
        
    return render(request, "nodes.html", {"nodes": nodes})