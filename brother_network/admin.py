"""
Brother network admin controllers
"""
from django.contrib import admin

from . import models


class ChapterAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

admin.site.register(models.Brother)
admin.site.register(models.Chapter, ChapterAdmin)
admin.site.register(models.Group)
admin.site.register(models.Event)
admin.site.register(models.Post)
