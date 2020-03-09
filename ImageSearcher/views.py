from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

# class-based view
class HelloWorld(TemplateView):
    template_name = 'test.html'