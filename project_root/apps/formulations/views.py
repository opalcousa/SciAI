from django.shortcuts import render
from django.http import JsonResponse
from .models import Formulation
import pandas as pd
import numpy as np

def list_formulations(request):
    formulations = Formulation.objects.all()
    formulation_list = list(formulations.values())
    return JsonResponse(formulation_list, safe=False)

def create_formulation(request):
    if request.method == 'POST':
        data = request.POST
        formulation = Formulation.objects.create(
            name=data['name'],
            raw_materials=data['raw_materials'],
            quantities=data['quantities']
        )
        formulation.save()
        return JsonResponse({'message': 'Formulation created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def update_formulation(request, formulation_id):
    if request.method == 'PUT':
        data = request.PUT
        formulation = Formulation.objects.get(id=formulation_id)
        formulation.name = data.get('name', formulation.name)
        formulation.raw_materials = data.get('raw_materials', formulation.raw_materials)
        formulation.quantities = data.get('quantities', formulation.quantities)
        formulation.save()
        return JsonResponse({'message': 'Formulation updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def delete_formulation(request, formulation_id):
    if request.method == 'DELETE':
        formulation = Formulation.objects.get(id=formulation_id)
        formulation.delete()
        return JsonResponse({'message': 'Formulation deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def calculate_formulation(request, formulation_id):
    if request.method == 'GET':
        formulation = Formulation.objects.get(id=formulation_id)
        raw_materials = pd.DataFrame(formulation.raw_materials)
        quantities = np.array(formulation.quantities)
        total_volume = np.sum(raw_materials['density'] * quantities)
        total_mass = np.sum(raw_materials['mass'] * quantities)
        return JsonResponse({'total_volume': total_volume, 'total_mass': total_mass}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)