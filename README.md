# Django meet-up
 - [tutorial](https://www.youtube.com/watch?v=t7DrJqcUviA&t=602s), [django rest framework](https://www.django-rest-framework.org/tutorial/quickstart/)
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
    -  