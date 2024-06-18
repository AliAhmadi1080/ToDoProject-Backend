from django.contrib import admin
from .models import Status, ToDo, Tag,ToDoList

admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(ToDoList)
admin.site.register(ToDo)