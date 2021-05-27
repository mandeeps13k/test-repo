FROM python:3.8.5-slim-buster
RUN mkdir /app
COPY . /app/

WORKDIR /app

RUN apt-get update && apt-get install python3-pip --yes && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
