from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("", views.home_welcome),
    path('hello/', views.say_hello),
    path("hello2/", views.say_hello2),
    path("hello3/", views.say_hello3),
    path('hello4/', views.say_hello4),
]
