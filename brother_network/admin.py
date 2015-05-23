"""
Brother network admin controllers
"""
from django.contrib import admin

from . import models


class BrotherAdmin(admin.ModelAdmin):
    list_filter = ['chapter']
    exclude = ['slug']
    search_fields = ['user', 'name']


class ChapterAdmin(admin.ModelAdmin):
    exclude = ['id']
    search_fields = ['id', 'name']

admin.site.register(models.Brother, BrotherAdmin)
admin.site.register(models.Chapter, ChapterAdmin)
admin.site.register(models.Group)
admin.site.register(models.Event)
admin.site.register(models.Post)
