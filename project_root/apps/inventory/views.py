from django.shortcuts import render
from django.http import JsonResponse
from .models import RawMaterial
from django.views.decorators.csrf import csrf_exempt
import json

def inventory_list(request):
    materials = RawMaterial.objects.all()
    materials_list = list(materials.values())
    return JsonResponse(materials_list, safe=False)

@csrf_exempt
def add_material(request):
    data = json.loads(request.body)
    material = RawMaterial.objects.create(
        name=data['name'],
        density=data['density'],
        price=data['price']
    )
    return JsonResponse({'id': material.id})

@csrf_exempt
def update_material(request, material_id):
    data = json.loads(request.body)
    RawMaterial.objects.filter(id=material_id).update(**data)
    return JsonResponse({'status': 'success'})

@csrf_exempt
def delete_material(request, material_id):
    RawMaterial.objects.filter(id=material_id).delete()
    return JsonResponse({'status': 'success'})