from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import TodoList

from django.views import View
from django.views import generic

#class Todo_board(generic, TemplateView):
class Todo_board(View):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_list.html'
        todo_list = TodoList.objects.all()
        return render(request, template_name, {"todo_list": todo_list})
# Create your views here.

