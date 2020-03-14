from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from ImageSearcher.models import Photo
from django.views.generic.edit import FormView

# import flickrapi
import flickrapi


def index(request):
    return render(request, 'search_form.html')

def search(request):
    if request.method == 'POST':
        search_key = request.POST.get('keyword', None)
        FLICKR_KEY = 'ae2852d2f6ba2975847022bbdd7cd8b3'
        FLICKR_SECRET = '126ce083bf676546'
        #userid 
        #FLICKR_USERID = '187361744@N02'
        try:
            flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format='parsed-json')
            # !!!Future expansion, let user inputs num of photos they want to search.
            photos = flickr.photos.search(text = search_key, per_page='20')["photos"]["photo"]
            if len(photos) == 0:
                return render(request,'no_responce.html')
            else:
                # render the photos on a new-webpage, allowing the user to select one of them.
                return render(request,'no_responce.html')

        except flickrapi.exceptions.FlickrError as err:
            # when searchAPI is not available
            return render(request, 'api_err.html')
    else:
        return render(request, 'search_form.html')


# view created for settup testing
class HelloWorld(TemplateView):
    template_name = 'test.html'


# view created for showing all searched photos
class PhotosView(ListView):
    # generate object list
    model = Photo
    template_name = 'photos.html'
