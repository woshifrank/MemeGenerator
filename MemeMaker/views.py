from django.shortcuts import render


from django.views.generic import TemplateView, ListView
from MemeMaker.models import Photo
from django.views.generic.edit import FormView
from django.http import HttpResponse
from MemeGenerator.settings import STATICFILES_DIRS

# Import flickrapi for searching.
import flickrapi
# Imports for making meme based on selected photos.
from PIL import Image, ImageDraw, ImageFont
import requests
import os
from io import BytesIO

def index(request):
    """The search page for the app.
    It prompts user to enter the keyword for Flickr searching

    Args:
        request: HttpRequest objects that contains metadata about the webpage request:
        http://localhost:8000/MemeMaker/

    Returns:
        The rendered index page.

    """
    # Suggestion for future development: Apart from search keyword,
    # also let user inputs num of photos they want on the page.
    return render(request, 'search_form.html')


def search(request):
    """Webpage that shows the results of flickr.photos.search api.
    It demonstrates the first 20 photos from flickr to the user
    and prompt him/her to select a photo as meme base by clicking on the photo.

    Args:
        request: HttpRequest objects that contains metadata about the webpage request:
        http://localhost:8000/MemeMaker/

    Returns:
        The rendered search result page. 

    """
    if request.method == 'POST':
        # Defined flickr key and secret for using flickr api.
        search_key = request.POST.get('keyword', None)
        FLICKR_KEY = 'ae2852d2f6ba2975847022bbdd7cd8b3'
        FLICKR_SECRET = '126ce083bf676546'

        try:
            flickr = flickrapi.FlickrAPI(
                FLICKR_KEY, FLICKR_SECRET, format='parsed-json')

            photos = flickr.photos.search(text=search_key, per_page='20')[
                "photos"]["photo"]

            if len(photos) == 0:
                return render(request, 'no_responce.html')
            else:
                # Collect the photo url sent by the api.
                # render each of them on the webpage.
                urls = []
                for photo in photos:
                    url = "http://farm{}.static.flickr.com/{}/{}_{}.jpg"\
                        .format(photo["farm"], photo["server"], photo["id"], photo["secret"])
                    urls.append(url)
                context = {"urls": urls}
                return render(request, 'search_result.html', context)

        except flickrapi.exceptions.FlickrError as err:
            # When searchAPI is not available, render the error page.
            return render(request, 'api_err.html')
    else:
        return render(request, 'search_form.html')


def memeChoice(request, photo_url):
    """Webpage that shows the selected picture and 
    prompts the users to enter the text they want to place in the meme.

    Args:
        request: HttpRequest objects that contains metadata about the webpage request:
            http://localhost:8000/MemeMaker/makeMeme/<path:selected_photo_url>
        photo_url: webpage url of the selected photo from flickr

    Returns:
        The rendered webpage.

    """
    # Future development suggestions: Prompt user to select/input
    # meme text's font and color.
    # Also prompt them to select whether text above/below/overlay the photo.
    context = {"selected_photo_url": photo_url}
    return render(request, 'meme_choice.html', context)


def memeShow(request, selected_photo_url):
    """Webpage that shows the generated meme. 
    It also contains a link for users to jump back to the search page for next meme.

    Args:
        request: HttpRequest objects that contains metadata about the webpage request:
            http://localhost:8000/MemeMaker/showMeme//<path:selected_photo_url>
        selected_photo_url: webpage url of the selected photo from flickr

    Returns:
        The rendered meme result page.

    """
    # Get the photo from url.
    web_response = requests.get(selected_photo_url)
    image = Image.open(BytesIO(web_response.content))

    draw = ImageDraw.Draw(image)
    # Use the default font and color is white.
    # For Future development, fetch font info and color from user's input.
    #font = ImageFont.load_default()
    font_path = os.path.join(STATICFILES_DIRS[0], 'Arial.ttf')
    font = ImageFont.truetype(font_path, size=45)
    color = 'rgb(255, 255, 255)'

    photo_width, photo_height = image.size
    memeText = request.POST.get('memeText', None)
    text_width, text_height = draw.textsize(memeText, font)

    # Create the overlay meme.
    # The inserted text is at the bottom middle of the photo.
    # For future version, user may be prompted to select the position.
    (x, y) = ((photo_width-text_width)//2, photo_height-text_height)
    draw.text((x, y), text=memeText, fill=color, font=font)

    # Save the image and render on the webpage.
    file_path = os.path.join(STATICFILES_DIRS[0], 'Meme.jpeg')
    image.save(file_path, 'JPEG')

    return render(request, 'meme_result.html')


class PhotosView(ListView):
    """Class-based view for demonstrating the searched result from Flickr.
    It is not adopted in the app, but created for future development.

    Returns:
        The rendered searched result page.

    """
    model = Photo
    template_name = 'photos.html'
