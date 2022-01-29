from django.urls import path, include
from . import views

from rest_framework import routers
from login.api import viewsets as userviewsets
route = routers.DefaultRouter()

route.register(r'/', userviewsets.UserViewset, basename="Users")

urlpatterns = [
    path('register', views.cad_user, name="cad_user"),
    path('list', views.show_users, name="list"),
    path('', include('django.contrib.auth.urls')),
    path('teste', include(route.urls))
]