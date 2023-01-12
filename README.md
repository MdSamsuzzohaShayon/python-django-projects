# Django Microservices
 - [tutorial](https://www.youtube.com/watch?v=ddrucr_aAzA&list=PLlameCF3cMEva65psDFX1y_gN2Tmh704t), [django rest framework](https://www.django-rest-framework.org/tutorial/quickstart/)
 - Making migrations
 ```
 docker compose exec backend_api_ser sh
 python manage.py makemigrations
 python manage.py migrate
 ```
- Api endpoints
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