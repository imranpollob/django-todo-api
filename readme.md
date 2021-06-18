## Creating a todo api using Django ret framework

Commands to follow

```bash
# creating virtual environment
python -m venv venv

# activating virtual environment
source venv/bin/activate

# installing django
pip install django

# installing django rest framework
pip install djangorestframework

# create requirement.txt file
pip freeze > requirements.txt

# start a new project named "Todo"
django-admin startproject todo .

# creating an app named "Api"
python manage.py startapp api

# create migration files
python manage.py makemigrations

# alternative command (preffered)
./manage.py makemigrations

# run migration (default sqlite)
./manage.py migrate

# create super/admin user
./manage.py createsuperuser

# run server
./manage.py runserver
```

Homepage 
```
http://127.0.0.1:8000/
```

Todo API 
```
http://127.0.0.1:8000/todos/
```