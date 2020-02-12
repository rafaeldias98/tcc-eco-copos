#!/bin/bash
python3 manage.py makemigrations --noinput
python3 manage.py migrate

cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.filter(username='${SUPERUSER_NAME}').exists() or \
    User.objects.create_superuser('${SUPERUSER_NAME}', '${SUPERUSER_EMAIL}', '${SUPERUSER_PASSWORD}')
EOF

if [ "$APPLICATION_ENV" == "development" ]; then
    python3 manage.py runserver 0.0.0.0:8000
else
    gunicorn tcc_eco_copos.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi
