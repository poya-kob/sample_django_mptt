from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Categories, Products

admin.site.register(Products)
admin.site.register(Categories, DraggableMPTTAdmin)
