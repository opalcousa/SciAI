from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('apps.inventory.urls')),
    path('projects/', include('apps.projects.urls')),
    path('formulations/', include('apps.formulations.urls')),
    path('ai_assistant/', include('apps.ai_assistant.urls')),
    path('user_interface/', include('apps.user_interface.urls')),
]