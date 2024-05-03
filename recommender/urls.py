"""recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.urls import include, path
from django.contrib import admin
from hotelhunter import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("signup/", views.signup, name="signup"),
]
# urlpatterns = [
#     path(r"^$", views.index, name="index"),
#     path(r"^search/", views.search, name="search"),
#     path(r"^signin/", views.signin, name="signin"),
#     path(r"^signup/", views.signup, name="signup"),
#     path(r"^signout/", views.signout, name="signout"),
# ]
