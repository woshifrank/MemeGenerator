# url configuration for app ImageSearcher
"""MemeGenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.urls import include
from MemeMaker.views import HelloWorld,PhotosView,index,search, memeChoice, memeShow

urlpatterns = [
    #path('', HelloWorld.as_view(), name = 'helloworld'),
    path('', index, name = 'searchPage'),
    path('searchResult/', search, name = 'searchResult'),
    path('makeMeme/<path:photo_url>', memeChoice, name = 'meme_generation_page'),
    path('showMeme/<path:selected_photo_url>', memeShow, name = 'meme_demonstration')
    #path('photos/', PhotosView.as_view(),name = 'photos')
]