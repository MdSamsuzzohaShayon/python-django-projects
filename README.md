# Django Rest framework
 - [tutorial](https://www.youtube.com/watch?v=c708Nf0cHrs&t=251s)
  - Product setup
    ```
    cd django_rest_framework_project/
    python3 -m venv virtual-env
    source virtual-env/bin/activate
    pip install -r requirements.txt 
    django-admin startproject drfhome .
    django-admin startapp api
    django-admin startapp products
    ./manage.py runserver
    ./manage.py makemigrations
    ./manage.py migrate
    ```
 - Add product from interactive shell `./manage.py shell`
   ```
   >>> Product.objects.create(title="sofa 1", content="best sofa", price=12.60)
   <Product: Product object (1)>
   >>> Product.objects.all().order_by("?").first()
   <Product: Product object (1)>
   >>> from products.models import Product
   >>> Product.objects.first()
   <Product: Product object (1)>
   >>> Product.objects.first().sale_price
   ```

 - Obstacle with django -> To serielize model to json data we get this error **TypeError: Object of type Decimal is not JSON serializable**
 - To get rid of this we should use django-rest-framework
 - Create super user `./manage.py createsuperuser`
 - Migrate whenever token authentication is used 
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
 - Token authentication properties from shell
  ```
  >>> from rest_framework.authtoken.models import *
  >>> locals()
  >>> Token
  >>> Token.objects.all()
  >>> dir(Token.objects.all().first())
  >>> token_obj = Token.objects.first()
  >>> token_obj.created
  ```







 https://www.youtube.com/watch?v=lo7lBD9ynVc
