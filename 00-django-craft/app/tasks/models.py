from django.db import models
from django.conf import settings

class Tag(models.Model):
  name = models.CharField(max_length=140)


class Skill(models.Model):
  name = models.CharField(max_length=140)


class Worker(models.Model):
  first_name = models.CharField(max_length=140)
  last_name = models.CharField(max_length=140)
  phone = models.CharField(max_length=15)
  email = models.EmailField(max_length=140)

  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="worker", null=True, on_delete=models.CASCADE)
  skills = models.ManyToManyField(Skill, related_name="skills", blank=True)

  def save(self, *args, **kwargs):
    if self._state.adding:
      self.user = settings.AUTH_USER_MODEL.objects.create_user(self.email, password=self.email)

    super().save(*args, **kwargs)


class Customer(models.Model):
  creation_datetime = models.DateTimeField(auto_now_add=True)
  last_update_datetime = models.DateTimeField(auto_now=True)

  company_name = models.CharField(max_length=140)
  contact_person = models.CharField(max_length=140)
  contact_phone = models.CharField(max_length=15)
  contact_email = models.EmailField(max_length=140)

  def __str__(self):
    return f"Customer #{self.id} ({self.name})"


class Project(models.Model):

  creation_datetime = models.DateTimeField(auto_now_add=True)
  last_update_datetime = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=140)
  description = models.CharField(max_length=256)

  manager = models.ForeignKey(Worker, related_name="projects_manager", null=True, default=None, on_delete=models.SET_NULL)
  members = models.ManyToManyField(Worker, related_name="projects")
  customer = models.ForeignKey(Customer, related_name="projects", null=True, on_delete=models.SET_NULL)

class Epic(models.Model):
  creation_datetime = models.DateTimeField(auto_now_add=True)
  last_update_datetime = models.DateTimeField(auto_now=True)

  name = models.CharField(max_length=128, unique=True)
  description = models.TextField(max_length=512, blank=True, null=True)
  deadline = models.DateField()

  project = models.ForeignKey(Project, related_name="epics", null=False, on_delete=models.CASCADE)


class Task(models.Model):
  creation_datetime = models.DateTimeField(auto_now_add=True)
  last_update_datetime = models.DateTimeField(auto_now=True)

  name = models.CharField(max_length=128, unique=True)
  description = models.TextField(max_length=512, blank=True, null=True)
  is_done = models.BooleanField(default=False)

  epic = models.ForeignKey(Epic, related_name="tasks", null=False, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, blank=True)

  def __str__(self):
    return f"Task #{self.id} ({self.name})"
#










