from django.contrib import admin

from .models import User, ShortUrl


class ShortUrlAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["url", "user"]}),
        ("Short Url", {"fields": ["key"]}),
    ]
    list_display = ("__str__", "url", "user")


admin.site.register(User)
admin.site.register(ShortUrl, ShortUrlAdmin)
