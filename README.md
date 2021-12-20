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


### Flask App
 - Run flask app `python3 filename.py` By default flask app runs on port number `5000`
 - Data migration in flask with MySQL `python3 manager.py db --help` (*Setup commands from manager.py file before running the command*)
 - Creates a new migration repository `python3 manager.py db init`
 - `sudo docker exec -it 62913dd99122 bash` go to container and migrate to the database `python manager.py db migrate`
 - `python manager.py db upgrade` once you upgrade you  can see all available tables
 - GO to this [site](https://www.cloudamqp.com/) and login/register -> create an instance
 - Copy AMQP url -> 


Time 57:00

 