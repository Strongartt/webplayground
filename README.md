WebPlayground - Proyecto CRUD con Django
Este es un proyecto básico desarrollado con el framework Django. Su principal objetivo es implementar una aplicación web funcional que permita realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre un modelo de páginas personalizadas.

El proyecto sigue la arquitectura MTV (Model - Template - View), equivalente al patrón MVC, utilizado comúnmente en el desarrollo web.

Tecnologías utilizadas
Python 3

Django

SQLite3

CKEditor (para contenido enriquecido)

HTML / CSS (a través de templates)

Estructura del proyecto
bash
Copiar
Editar
webplayground/
├── core/               # App principal
├── pages/              # App para gestión de páginas (CRUD)
├── webplayground/      # Configuración general del proyecto
├── db.sqlite3          # Base de datos SQLite
└── manage.py           # Script de gestión del proyecto
Arquitectura MTV aplicada
Modelo (models.py)
En el archivo pages/models.py se define el modelo Page que contiene los campos:

title: Título de la página

content: Contenido enriquecido (usando CKEditor)

order: Orden de aparición

created: Fecha de creación

updated: Fecha de edición

Vista (Controlador - views.py)
Las funciones de vista son:

python
Copiar
Editar
def pages(request):
    # Lista todas las páginas
    ...

def page(request, page_id, page_slug):
    # Muestra el detalle de una página
    ...
Estas vistas actúan como Controlador: consultan el modelo y pasan los datos a las plantillas.

URLs (urls.py)
En pages/urls.py se definen las rutas:

python
Copiar
Editar
urlpatterns = [
    path('', views.pages, name='pages'),
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]
Templates
Las plantillas se encargan de mostrar los datos al usuario. Se utiliza pages.html para listar y page.html para mostrar el detalle.

Operaciones CRUD
Acción	Descripción
Create	Crear nuevas páginas desde el panel admin
Read	Ver páginas en la web mediante vistas
Update	Editar páginas desde el panel admin
Delete	Eliminar páginas desde el panel admin
El proyecto implementa un CRUD completo utilizando Django Admin para las operaciones de crear, actualizar y eliminar, mientras que las vistas personalizadas (pages y page) gestionan la operación de lectura (read) pública para los usuarios.

¿Cómo ejecutar el proyecto?
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/Strongartt/webplayground.git
Entra en la carpeta del proyecto:

bash
Copiar
Editar
cd webplayground
Instala dependencias manualmente (si es necesario):

bash
Copiar
Editar
pip install django
pip install django-ckeditor
Aplica migraciones y ejecuta el servidor:

bash
Copiar
Editar
python manage.py migrate
python manage.py runserver
Accede a la aplicación en tu navegador:
http://127.0.0.1:8000/

Créditos
Desarrollado por: Ricardo Perez
GitHub: Strongartt
Proyecto académico para demostrar el uso de Django con el patrón MVC y operaciones CRUD.

Licencia
Este proyecto se distribuye bajo licencia educativa. Puedes modificarlo libremente para uso académico y aprendizaje.

Este proyecto no incluye un archivo requirements.txt ya que todas las dependencias necesarias están instaladas localmente y el proyecto funciona correctamente.








