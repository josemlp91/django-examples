from django import forms


class SimpleForm(forms.Form):
  name = forms.CharField(label='Nombre', max_length=100)
  email = forms.EmailField(label='Correo electrónico')

  def clean_email(self):
    email = self.cleaned_data['email']
    if not email.endswith('.com'):
      raise forms.ValidationError("El correo electrónico debe terminar en '.com'")
    return email


###########

from .models import *


class TaskSimpleForm(forms.Form):
  name = forms.CharField(label='Nombre', max_length=128)
  description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'rows': 3}))
  is_done = forms.BooleanField(label='¿Está hecho?', required=False)
  epic = forms.ModelChoiceField(label='Épica', queryset=Epic.objects.all())
  tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.all(), required=False)

  def clean_name(self):
    name = self.cleaned_data['name']
    if Task.objects.filter(name=name).exists():
      raise forms.ValidationError("Ya existe una tarea con este nombre.")
    return name


class TaskModelForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'description', 'is_done', 'epic', 'tags']
