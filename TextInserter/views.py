from django.shortcuts import render
from django.views.generic import TemplateView
# Class-based view
class HelloWorld(TemplateView):
    template_name = 'test.html'