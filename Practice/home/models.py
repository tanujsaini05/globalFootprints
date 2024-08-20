from django.db import models
from django.utils.translation import gettext_lazy as _

class Blog(models.Model):

    FESTIVAL = 'FEST'
    CULTURAL = 'CL'
    ADVENTURE = 'AD'

    CATEGORY_CHOICES = [
        (FESTIVAL, _('Festival')),
        (CULTURAL, _('Cultural')),
        (ADVENTURE, _('Adventure')),
    ]

    title = models.CharField(max_length=100)
    time = models.TimeField()
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=5,
        choices=CATEGORY_CHOICES,
        default=FESTIVAL,
    )