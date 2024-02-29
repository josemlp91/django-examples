from django.core.management.base import BaseCommand

from tasks.models import Task


class Command(BaseCommand):
  help = 'List all tasks'

  def handle(self, *args, **options):
      tasks = Task.objects.all()
      for t in tasks.iterator():
        print(t)
