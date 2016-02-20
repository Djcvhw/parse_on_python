from django.contrib import admin
from .models import Url, Info

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'timeshift')

admin.site.register(Url, UrlAdmin)
admin.site.register(Info)