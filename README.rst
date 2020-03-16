=====
MemeMaker
=====
MemeMaker is a Django app that I create for Academic Innovation Software Development Fellowship.
It will enable users to search for images on Flickr with a given string, and select the one they 
prefer and create a meme based on it. 

MemeGenerator is the name of my django project, and MemeMaker is the actual application for it. 

Quick start
-----------
1. Extract MemeGenerator.zip to a directory.

2. Open the directory in terminal. Run 'pipenv install' command in the directory. After pipenv is set up,
activate the environment with 'pipenv shell'

3. Start the server with 'python manage.py runserver'

4. Visit http://127.0.0.1:8000/MemeMaker/  to search in Flickr and create a meme.

4. For future development, you may visit http://127.0.0.1:8000/admin/ and sign in as admin with:
username:yijiefrank, password: woshifrank.
However, since I did not adopt class-view during my development, the 'Photos' in MEMEMAKER section is still unapplicable.

