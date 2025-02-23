from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    
    def __str__(self):
        return f"Node '{self.name}' has {self.children.count()} children"
    
    def print_children(self):
        children = self.children.all()
        print(f"Children of Node '{self.name}':")
        for child in children:
            print(child.name)