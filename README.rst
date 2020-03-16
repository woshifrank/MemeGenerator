=====
MemeMaker
=====
MemeMaker is a Django app that I create for Academic Innovation Software Development Fellowship.
It will enable users to search for images on Flickr with a given string, and select the one they 
prefer and create a meme based on it. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "MemeMaker" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'MemeMaker',
    ]

2. Include the MemeMaker URLconf in your project urls.py like this::

    path('MemeMaker/', include('MemeMaker.urls')),

3. Run ``python manage.py migrate`` to create the MemeMaker models.

4. Visit http://127.0.0.1:8000/MemeMaker/  to search in Flickr and create a meme.

5. For future development, you may visit http://127.0.0.1:8000/admin/ and sign in as admin with:
username:yijiefrank, password: woshifrank.
However, since I did not adopt class-view during my development, the 'Photos' in MEMEMAKER section is still unapplicable.

