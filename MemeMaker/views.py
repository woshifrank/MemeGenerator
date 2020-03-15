from django.shortcuts import render


from django.views.generic import TemplateView, ListView
from MemeMaker.models import Photo
from django.views.generic.edit import FormView
from django.http import HttpResponse
from MemeGenerator.settings import STATICFILES_DIRS

# import flickrapi for searching
import flickrapi
# imports for making meme based on selected photos
from PIL import Image, ImageDraw, ImageFont
import requests,os
from io import BytesIO


def index(request):
    return render(request, 'search_form.html')


def search(request):
    if request.method == 'POST':
        search_key = request.POST.get('keyword', None)
        FLICKR_KEY = 'ae2852d2f6ba2975847022bbdd7cd8b3'
        FLICKR_SECRET = '126ce083bf676546'

        try:
            flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format='parsed-json')
            # !!!Future expansion, let user inputs num of photos they want to search.
            photos = flickr.photos.search(text = search_key, per_page='20')["photos"]["photo"]
            if len(photos) == 0:
                return render(request,'no_responce.html')
            else:
                # render the photos on a new-webpage, allowing the user to select one of them.
                urls = []
                for photo in photos:
                    # http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}.jpg 
                    url = "http://farm{}.static.flickr.com/{}/{}_{}.jpg"\
                        .format(photo["farm"], photo["server"], photo["id"], photo["secret"])
                    urls.append(url)
                context = {"urls":urls}
                return render(request,'search_result.html',context)

        except flickrapi.exceptions.FlickrError as err:
            # when searchAPI is not available
            return render(request, 'api_err.html')
    else:
        return render(request, 'search_form.html')


def memeChoice(request,photo_url):
    context = {"selected_photo_url" : photo_url }
    return render(request, 'meme_choice.html', context)

def memeShow(request,selected_photo_url):
    # get the photo from url
    web_response = requests.get(selected_photo_url)

    image = Image.open(BytesIO(web_response.content))
    # create the overlay meme. 
    # The inserted text is at the bottom middle of the photo
    draw = ImageDraw.Draw(image)

    # TODO ！ SELECTION OF fONT and color FOR FUTURE DEVELOPMENT
    font = ImageFont.truetype("arial.ttf", size=45)
    # set the color as black
    color = 'rgb(255, 255, 255)' 

    photo_width, photo_height = image.size
    memeText = request.POST.get('memeText', None)
    text_width, text_height = draw.textsize(memeText, font)

    # insert the text into the image
    (x,y) = ((photo_width-text_width)//2, photo_height-text_height)
    draw.text((x, y), text = memeText, fill=color, font=font)

    # save the image and render on the webpage.
    file_path = os.path.join(STATICFILES_DIRS[0] , 'Meme.jpeg')
    #html = '<div>%s</div>'%file_path
    #return HttpResponse(html)
    image.save(file_path, 'JPEG')
    #, "JPEG"
    
    return render(request, 'meme_result.html')


# view created for settup testing
class HelloWorld(TemplateView):
    template_name = 'test.html'


# view created for showing all searched photos
class PhotosView(ListView):
    # generate object list
    model = Photo
    template_name = 'photos.html'
