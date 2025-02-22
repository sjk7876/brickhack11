from django.contrib import admin
from .models import Node

class ChildInline(admin.TabularInline):
    model = Node
    fk_name = "parent"
    extra = 1  # Adjust the number of empty forms as needed
    
    def verbose_name_plural(self):
        return "Children"


class NodeAdmin(admin.ModelAdmin):
    fields = ["name", "image", "parent"]
    inlines = [ChildInline]

admin.site.register(Node, NodeAdmin)
