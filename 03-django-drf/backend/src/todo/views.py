from django.http import JsonResponse
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

from .tasks import *

def demo(requets):
  xsum.delay([i for i in range(100000)])
  return JsonResponse({'result': 'ok'})


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
