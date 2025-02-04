# hier werden die Models festgelegt auf die der Admin auf der /admin/ Page zugreifen kann.

from django.contrib import admin
from .models import Kommentare

# Register your models here.
admin.site.register(Kommentare)