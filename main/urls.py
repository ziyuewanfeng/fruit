from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^checkout', views.checkout, name="checkout"),
    url(r'^register', views.register, name="register"),
]
