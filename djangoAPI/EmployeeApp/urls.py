from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi)
]