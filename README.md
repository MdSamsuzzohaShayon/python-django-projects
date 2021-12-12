# Django vue ecommerce

 - [tutorials](https://www.youtube.com/watch?v=Yg5zkd9nm6w&t=3476s)
 - make project and setup project with virtual environment
```
mkdir python-django-vuejs
cd python-django-vuejs/
ls
git init
pip install virtualenv
virtualenv environment_3_8_1
source environment_3_8_1/bin/activate
```

 - Install all essential package or dependencies
```
pip install django
python3 -m pip install --upgrade pip
pip install django
pip install django-rest-framework
pip install django-cors-headers
pip install djoser
pip install pillow
pip install stripe
```

 - create ne django project `django-admin startproject movie_ecom`
 - initialize database
```
pip list
pip freeze > requirements.txt 
ls
cd movie_ecom/
echo "initilize database"
python3 manage.py makemigrations
python3 manage.py migrate
```
 - creating super user for admin
```
python3 manage.py createsuperuser
# username - admin
# password - 1234
```
 - __http://localhost:8000/admin__
 - Install and setup vue js
```
vue create movie_ecom_vue
cd movie_ecom_vue/
npm install axios
npm audit fix
npm install bootstrap
npm run serve
```
 - 




