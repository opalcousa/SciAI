from django.contrib import admin
from .models import RawMaterial

class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'density', 'price')
    search_fields = ['name']

admin.site.register(RawMaterial, RawMaterialAdmin)