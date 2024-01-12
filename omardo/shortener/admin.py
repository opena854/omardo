from django.contrib import admin

from .models import User, ShortUrl

admin.site.register(User)
admin.site.register(ShortUrl)
