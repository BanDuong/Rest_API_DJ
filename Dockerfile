FROM python:3.9

ENV PYTHONUNBUFFERED=1

ghfhjgjkhj

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 80

CMD exec uwsgi --http :80 --module config.wsgi
#CMD python manage.py runserver
