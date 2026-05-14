# How to create "Hello world with Django"

## Setup

* Create a virtual environment
* First step you need to create new virtual environment with python, with following command

``` /usr/bin/python3 -m venv django_venv ```

* source django_venv/bin/activate

* then activate your environment

``` source django_venv/bin/activate ```

* to exit your virtual environment

``` deactivate ```

##  Create your project

* You need to create a new project Django, take care follow this command in the directory where you want your project

``` django-admin startproject mysite djangotutorial ```

* You can reactivate your virtual environment and run this

``` python manage.py runserver ```

* To create your application, make sure you are in the same directory as manage.py and enter this command

```python manage.py startapp polls```

## Write your first view

* Open the polls/views.py file and place the following Python code

``` 
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
```
* Open the urls.py file and place the following Python code

``` 
from django.urls import path
from . import  views

urlpatterns = [
    path("", views.index, name="index"),
]

```
* The next step is to configure the root URLconf of the mysite project to include the URLconf defined in polls.urls. To do this, add a django.urls.include import into mysite/urls.py and insert a call to include() in the urlpatterns list, which will give

``` 
from django.contrib import admin
from django.urls import include, path

urlpatterns =  [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```  
<br>

    
<br>

## helpful command

|Command|Description|
|-------|-----------|
|`pip list` | use this command on your virtual environment for list package installed on this  |
|`pip install <package>`            | install a package |
|`pip uninstall <package>`          | desinstall a package |
|`pip freeze > requirements.txt`    | save the packages |
|`pip install -r requirements.txt`  | install package from a file un requirements.txt |
|`python manage.py runserver`       | launch server |
|`python manage.py startapp <name>` | create application |
|`python manage.py migrate`         | apply migration |
|`python manage.py makemigrations`  | create migration |
|`python manage.py createsuperuser` | create an admin |
|`source venv/bin/activate`         | activate |
|`deactivate`                       | desactivate  |