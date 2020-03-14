from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from ImageSearcher.models import Photo
from django.views.generic.edit import FormView

# import flickrapi
import flickrapi

# view created for settup testing
class HelloWorld(TemplateView):
    template_name = 'test.html'

# view created for showing all searched photos
class PhotosView(ListView):
    # generate object list
    model = Photo
    template_name = 'photos.html'
