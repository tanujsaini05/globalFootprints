from django.contrib import admin
from .models import Blog

##Register the Blog model with the admin site
admin.site.register(Blog)
admin.site.index_title="Welcome"
