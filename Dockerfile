FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python3 manage.py makemigrations \
    && python3 manage.py migrate

COPY ./ .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

