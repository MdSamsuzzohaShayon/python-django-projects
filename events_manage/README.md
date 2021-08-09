 - Initial set up
 ```
virtualenv env_3_8_1
source env_3_8_1/bin/activate
python3 -m pip install Django
git rm -rf --cached .
git add .
git commit -m "clean up"
django-admin startproject events_manage
cd events_manage/
python3 manage.py startapp meetups
```

-Structire database and execute
```
 python3 manage.py makemigrations
 python3 manage.py migrate
```


