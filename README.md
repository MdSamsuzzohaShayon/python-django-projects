# Django vue ecommerce

 - [tutorials](https://www.youtube.com/watch?v=y69VDOczkik)
 - Installation
```
    pip install djangorestframework
    pip install Django
    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
    pip install mysqlclient
    pip install django-mysql
    pip install django-cors-headers
    pip install pike
```
 - Docker commands
```
    sudo docker-compose up --build -d
    sudo docker ps -a
    sudo docker logs django-microservice
    sudo docker-compose down -v
    sudo docker ps -a
    sudo docker images
    sudo docker image rm 186215183cfc -f
    sudo docker images 
    sudo docker image rm django-microservice-image -f
    sudo docker-compose up --build -d
```
 - Connect to MySQL Database (take few minutes to start mysql) `mysql -h localhost -P 3307 --protocol=tcp -u admin -p`
 - Interact with container `sudo docker exec -it django-microservice bash`
 - Create new app from container `python manage.py startapp products`
 - phpmyadmin connection 
    - server : db
    - username: admin
    - password: admin
 - 
 