from django.urls import path
from app3.views import *
app_name="paru"

urlpatterns=[
    path("app3/",app3,name='app3')
]