from django.urls import path
from . import views

app_name = 'user_interface'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_material/', views.new_material, name='new_material'),
    path('edit_material/<int:material_id>/', views.edit_material, name='edit_material'),
    path('delete_material/<int:material_id>/', views.delete_material, name='delete_material'),
    path('new_formulation/', views.new_formulation, name='new_formulation'),
    path('edit_formulation/<int:formulation_id>/', views.edit_formulation, name='edit_formulation'),
    path('delete_formulation/<int:formulation_id>/', views.delete_formulation, name='delete_formulation'),
    path('calculate_cost/<int:formulation_id>/', views.calculate_cost, name='calculate_cost'),
    path('ai_assistant/', views.ai_assistant, name='ai_assistant'),
]