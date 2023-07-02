from django.shortcuts import render
from django.http import JsonResponse
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    project_list = list(projects.values())
    return JsonResponse(project_list, safe=False)

def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    return JsonResponse({'name': project.name, 'description': project.description})

def project_create(request):
    if request.method == 'POST':
        data = request.POST
        project = Project.objects.create(name=data.get('name'), description=data.get('description'))
        return JsonResponse({'message': 'Project created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def project_update(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    if request.method == 'PUT':
        data = request.POST
        project.name = data.get('name', project.name)
        project.description = data.get('description', project.description)
        project.save()
        return JsonResponse({'message': 'Project updated successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def project_delete(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    if request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'Project deleted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)