FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN python manage.py makemigrations

RUN python manage.py migrate --run-syncdb

EXPOSE 8000