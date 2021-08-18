from django.urls import path
from . import views

urlpatterns = [
    path(r'index/', views.index, name = 'index'),
    path(r'login/', views.login, name = 'login'),
    path(r'login/login_ok/', views.login_ok, name = 'login_ok'),
    path(r'table/', views.table, name = 'table'),
]