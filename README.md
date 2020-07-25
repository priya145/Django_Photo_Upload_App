# Photo Upload App
A progressive photo upload app built with Django 3.0.5. Multiple users can upload photos on their Profile and make their own photo gallery.
***
## Features
- Multiple user login and signup with JWT authentication.
- Photo uploading functionality with upload progress bar.
- Only the uploaded user can view their photos on their profile after login.
***
## Requirements
- Django = 3.0.5
- python = 3.7.3
- django-crispy-forms = 1.9.0
- Pillow = 7.1.2
- djangorestframework = 3.11.0
- django-progressive-web-app
***
## INSTALLED_APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'homepage',
    'crispy_forms',
    'rest_framework',
    'rest_framework_jwt',
    'rest_framework_swagger',
    'django_extensions',
    'rest_framework.authtoken',
    'rest_auth',
    'pwa'
]
```
***
## urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('homepage/',include('homepage.urls')),
    path('', include('pwa.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
***
## How to run it
- to migrate the database
```
$ cd photouploadapp
$ python manage.py makemigrations
$ python manage.py migrate
```
- to run the program
```
python manage.py runserver
```
Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).Open the address in the browser
***
## Project Tree
```
├── photouploadapp
    ├── user
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── migrations
    │   ├── tests.py
    │   ├── forms.py
    │   └── tokens.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── db.sqlite3
    ├── manage.py
    │
    ├── media   
    │   └── uploads
    │
    ├── photouploadapp
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── static
    │   └── icons
    │   └── manifest.webmanifest
    │   └── photouploadapp
    │       ├── css
    │       ├── js
    │       ├── fonts
    │       ├── img
    │
    ├── templates
    │   ├── user
    │   ├── homepage
    │       ├── serviceworker.js
    │
    ├── homepage
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── migrations
    │   ├── tests.py
    │   ├── forms.py
    │   ├── urls.py
    │   └── views.py
 ```
