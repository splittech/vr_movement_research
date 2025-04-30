FROM python:3.11-slim as build
LABEL authors="Stepanov V.A."

COPY . /app/

RUN mkdir /modules \
    && apt-get update && apt-get install -y curl && apt-get clean \
    && pip install --upgrade pip \
    && pip install --target /modules -r /app/requirements.txt


FROM python:3.11-slim as django
LABEL authors="Stepanov V.A."

WORKDIR /app/

COPY --from=build /app/ /app/
COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY --from=build /modules /modules

RUN pip install gunicorn

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /modules

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" \
    && python manage.py collectstatic --no-input \
    # && python manage.py runserver 0.0.0.0:8000
    && gunicorn vr_movement_research.wsgi:application --bind 0.0.0.0:8000 --log-level info