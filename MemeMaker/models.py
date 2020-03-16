from django.db import models
from imagekit.models import ProcessedImageField


class Photo(models.Model):
    """This model is created for future development.
    It will enable user to store their search results or memes in database.
    """
    url = models.TextField(blank=True, null=True)
    inserted_text = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/photos',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )
