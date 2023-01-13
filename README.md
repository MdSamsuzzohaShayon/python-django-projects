# Django Microservices
 - [tutorial](https://www.youtube.com/watch?v=ddrucr_aAzA&list=PLlameCF3cMEva65psDFX1y_gN2Tmh704t), [django rest framework](https://www.django-rest-framework.org/tutorial/quickstart/)
 - Making migrations
 ```
 docker compose exec backend_api_ser sh
 python manage.py makemigrations
 python manage.py migrate
 ```
- Django admin app API endpoints
    - `/api/products` list all products `curl http://localhost:8000/api/products`
    - `/api/products` create a product `curl -X POST http://localhost:8000/api/products -H 'Content-Type: application/json' -d '{"title": "title1", "image": "image1.jpg"}'`
    - `/api/products/1` Get single product `curl http://localhost:8000/api/products/1`
    - `/api/products/1` Update a product `curl -X PUT http://localhost:8000/api/products/1 -H 'Content-Type: application/json' -d '{"title": "title1 update", "image": "update/image1.jpg"}'`
    - `/api/products/1` Delete a product `curl -X DELETE http://localhost:8000/api/products/2`
    - `/api/user` get a random user `curl -X GET http://localhost:8000/api/user`

 - Create user in database manually
  ```
  docker exec -it mysql_admin_con bash
  mysql -u root -p
  use admin;
  insert into products_user(id) values (2);
  insert into products_user(id) values (1);
  insert into products_user(id) values (3);
  ```

 - Flask main app API endpoints
    - `/` testing api `curl http://localhost:8001`
 - Was not able to use mysql with sqlalchemy due to an error. I had to use sqlite instead

### Rabbitmq
 - [Getting started with Rabbit MQ](https://www.youtube.com/watch?v=x98-JfEV7IA)
 - Create an account in [Cloud AMPQ](https://customer.cloudamqp.com/) and login, 
 - Create a new free instance -> overview -> copy ampq url
 - Completed previous 6 tutorial now [start from 7](https://www.youtube.com/watch?v=hi8DjlcbN4A&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO&index=8)
 - [Learn RabbitMQ In 30 Minutes](https://www.youtube.com/watch?v=QfsXKdm0uys)
 - [Dockerize your Django App - Add Celery Task Runner and RabbitMQ](https://www.youtube.com/watch?v=9RQpUv9QRJY)
 