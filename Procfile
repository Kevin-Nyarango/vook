web: gunicorn kportfolio.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate