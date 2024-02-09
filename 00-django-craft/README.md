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


## Guión Docker

```bash
make newproject
make newapp name=todo
make up
```
