from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
class Photo(models.Model):
    title = models.TextField(blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/photos',
        format = 'JPEG',
        options = {'quality' : 100},
        blank = True,
        null = True
    )