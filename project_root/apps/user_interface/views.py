from django.shortcuts import render
from apps.inventory.models import RawMaterial
from apps.projects.models import Project
from apps.formulations.models import Formulation
from apps.ai_assistant.models import AIAssistant

def home(request):
    raw_materials = RawMaterial.objects.all()
    projects = Project.objects.all()
    formulations = Formulation.objects.all()
    ai_assistant = AIAssistant.objects.first()

    context = {
        'raw_materials': raw_materials,
        'projects': projects,
        'formulations': formulations,
        'ai_assistant': ai_assistant,
    }

    return render(request, 'user_interface_detail.html', context)