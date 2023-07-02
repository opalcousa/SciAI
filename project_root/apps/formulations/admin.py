from django.contrib import admin
from .models import Formulation

@admin.register(Formulation)
class FormulationAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_volume', 'total_mass', 'cost')
    search_fields = ('name',)
    ordering = ('name',)