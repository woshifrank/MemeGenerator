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

2. Open the directory in terminal. Make sure pipenv and python3.8 are installed

3. Run 'pipenv install' command in the directory. After pipenv is set up,
activate the environment with 'pipenv shell'

4. Install django with 'pipenv install django'. 

5. Start the server with 'python manage.py runserver'

6. Visit http://127.0.0.1:8000/MemeMaker/  to search in Flickr and create a meme.

7. For future development, you may visit http://127.0.0.1:8000/admin/ and sign in as admin with:
username:yijiefrank, password: woshifrank.
However, since I did not adopt class-view during my development, the 'Photos' in MEMEMAKER section is still unapplicable.

8. Current font adopts is Arial. The Arial.ttf file in the static folder are added as the current font source for texts in meme. This solves the conflicts during which MacOS and Windows use different
naming conventions for their font files. For Future development font selection can be added for users.  

