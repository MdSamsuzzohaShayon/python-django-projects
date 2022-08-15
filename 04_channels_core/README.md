# Django docker chat app

- Django channels [tutorial](https://www.youtube.com/watch?v=D43IitXdqk0&t=1s)


### docker
 - Dockerfile (Everything is working without docker compose)
```
FROM python:3.10.6-alpine3.15
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

 - Build image
```
sudo docker build -t django_chat_image .
```
 - Running container

```
sudo docker run -d -p 8000:8000 --rm -v $"PWD":/app:ro -v /app/virtual-env -w /app --name django_channels_core_con django_chat_image
```

 - See container
```
sudo docker exec -it django_channels_core_con sh
```
 - See logs
```
sudo docker logs django_channels_core_con
```
### Docker compose
 - Build from docker compose
```
sudo docker compose up -d --build
```
 - Remove container
```
sudo docker compose down -v
```
 - Use [web socket king](https://websocketking.com/) for testing similer to postman for http
- Create django superuser
```
`sudo docker compose run web python3 manage.py migrate`
sudo docker compose run web python3 manage.py createsuperuser
```
