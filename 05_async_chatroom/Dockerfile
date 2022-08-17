#FROM python:3.10-alpine
FROM python:3.10
#FROM python:3.10.6-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

#RUN apt install python-dev  \
#    && apt install build-essential

RUN pip3 install --upgrade setuptools \
    && pip3 install --upgrade pip \
    && pip install -r requirements.txt


#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]