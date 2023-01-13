FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

#CMD uvicorn main:app --reload --port 5000
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]