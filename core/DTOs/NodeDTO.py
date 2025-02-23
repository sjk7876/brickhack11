import json

class NodeDTO:
    def __init__(self, id, name, image, children):
        self.id = id
        self.name = name
        self.image = image
        self.children: list[NodeDTO] = children
        
    def __repr__(self):
        return f"NodeDTO(name={self.name}, image={self.image}, children={self.children})"
        
def load_nodes_from_json(filepath="core/testdata/nodes.json"):
    with open(filepath, "r") as file:
        data = json.load(file)
    
    nodes = []
    for node_dict in data:
        node = load_node(node_dict)
        nodes.append(node)
    return nodes

def load_node(node_dict):
    children = []
    for child_dict in node_dict['children']:
        node = NodeDTO(child_dict["id"], child_dict['name'], child_dict['image'], load_node(child_dict))
        children.append(node)
    return NodeDTO(node_dict["id"], node_dict['name'], node_dict['image'], children)