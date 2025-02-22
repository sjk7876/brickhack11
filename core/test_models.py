from django.test import TestCase
from .models import Node

class NodeTestCase(TestCase):
    def test_str_method(self):
        # Create a node with some children
        parent = Node.objects.create(name='Fruits')
        apple = Node.objects.create(name='Apple', parent=parent)
        banana = Node.objects.create(name='Banana', parent=parent)

        # Check that the str method returns the correct string
        self.assertEqual(str(parent), "Node 'Fruits' has 2 children")

    def test_str_method_no_children(self):
        # Create a node with no children
        node = Node.objects.create(name='Vegetables')

        # Check that the str method returns the correct string
        self.assertEqual(str(node), "Node 'Vegetables' has 0 children")

    def test_print_children(self):
        # Create a node with some children
        parent = Node.objects.create(name='Fruits')
        apple = Node.objects.create(name='Apple', parent=parent)
        banana = Node.objects.create(name='Banana', parent=parent)

        parent.print_children()
