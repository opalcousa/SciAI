from django.urls import path
from . import views

app_name = 'formulations'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:formulation_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:formulation_id>/update/', views.update, name='update'),
    path('<int:formulation_id>/delete/', views.delete, name='delete'),
]