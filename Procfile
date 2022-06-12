release: python manage.py migrate; python manage.py createsuperuser

web: gunicorn FoodAppServer.wsgi --log-file -