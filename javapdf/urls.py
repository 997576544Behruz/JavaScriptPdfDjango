from django.urls import path
from .views import *

urlpatterns=[
    path('',addhome,name="addhome"),
    path('home/',Home,name="home"),
    path('updateblog/<str:id>',UpdateBlog,name="updateblog"),

]