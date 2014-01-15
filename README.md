todo-rest
=========

Todo app with Django REST Framework and AngularJS.

Installation:
> virtualenv todo-rest-env -p /usr/bin/python2.7

> cd todo-rest-env

> source bin/activate

> git clone https://github.com/jrvidotti/todo-rest.git

> cd todo-rest

> pip install -r requirements.txt

Create database and a superuser:

> python manage.py syncdb --migrate

> python manage.py runserver

Open url in Firefox browser with Firebug activated to watch requests being sent to REST backend: 

> http://localhost:8000/tasks
