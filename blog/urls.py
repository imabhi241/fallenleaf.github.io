from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("trending", views.trending, name="trending"),
    path("contact", views.contact, name="contact"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login")


    
    
]