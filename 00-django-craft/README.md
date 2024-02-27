# Crear una aplicación Django de 0


## Guión virtualenv

```bash

# Crear nuevo virtualenv
virtualenv venv

# Activar el virtualenv en la shell actual
. venv/bin/activate

# Instalar paquetes python en virtualenv
pip install -r requirements.txt

# Iniciar un proyecto django dentro del directorio /app
django-admin startproject main ./app

# Iniciar una aplicación llamada task en el proyecto
cd app
django-admin startapp tasks

# Crear base de datos y tablas
python manage.py migrate

# Iniciar servidor web
python manage.py runserver 0.0.0.0:8000
```


## Mini ejercicios

- [] Revisar settings y buscar en la documentación aquellas variables que desconozcamos
- [] Crear una vista que diga hola mundo, creando una plantilla html
- [] Crear una vista JSON
- [] Crear un modelo, generar migraciones y ejecutarlas
- [] Añadir el modelo al admin
- [] Crear un formulario
- [] Crear vista que interactue con el formulario
- [] Crear un commando
- [] Crear modelos dado un diagrama ER más complejo

```
from datetime import datetime
from django.db.models import Q
from django.db.models import Sum, Avg

today = datetime.today()
company_name = "TechCorp"
worker_first_name = "Lala"
project_id = 1

member = Worker.objects.get(first_name=worker_first_name)
customer = Customer.objects.get(company_name=company_name)

customer_tasks = Task.objects.filter(epic__project__customer=customer)
deadlined_task = Task.objects.filter(epic__deadline__lte=today)
print(deadlined_task.query)

worker_manager_tasks = Task.objects.filter(Q(epic__project__manager=member) | Q(epic__project__members=member))
print(worker_manager_tasks.query)

project_estimated_hours = Task.objects.filter(epic__project_id=project_id).aggregate(total_hours=Sum('estimated_hours'))
print(project_estimated_hours.query)

tasks_count_per_epic = Epic.objects.annotate(num_tasks=Count('tasks'))
tasks_count_per_epic[0].name
tasks_count_per_epic[0].num_tasks

project_count_per_worker = Worker.objects.annotate(num_projects=Count('projects'))
project_count_per_worker[0].first_name
project_count_per_worker[0].num_projects
```

## Guión Docker

```bash
make newproject
make newapp name=todo
make up
```
