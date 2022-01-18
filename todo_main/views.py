from django.shortcuts import render, redirect

from django.views import View
from django.views import generic
from django.views.generic.base import TemplateView


#class Todo_main(generic,TemplateView):
class Todo_main(View):   
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        return render(request, template_name)

# Create your views here.
