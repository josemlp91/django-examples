from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .forms import SimpleForm

def index(request, name=None):
  context = {"name": name, "skills": ["python", "javascript", "docker", "mongo"]}
  return render(request, 'index.html', context)


def api(request, name=None):
  dict = {"name": name, "skills": ["python", "javascript", "docker", "mongo"]}
  return JsonResponse(dict, status=200)

def myform(request):
  if request.method == 'POST':
    form = SimpleForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      return render(request, 'form.html', {'name': name, 'email': email})
  else:
    form = SimpleForm()

  return render(request, 'form.html', {'form': form})

from .forms import TaskSimpleForm, TaskModelForm
from .models import Task

def create_task(request):
  if request.method == 'POST':
    form = TaskModelForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      description = form.cleaned_data['description']
      is_done = form.cleaned_data['is_done']
      epic = form.cleaned_data['epic']
      tags = form.cleaned_data['tags']

      tarea = Task.objects.create(name=name, description=description, is_done=is_done, epic=epic)
      tarea.tags.set(tags)

      messages.add_message(request, messages.INFO, "Tarea creada con éxito")
      return redirect('index')
  else:
    form = TaskModelForm()
  return render(request, 'form.html', {'form': form})
