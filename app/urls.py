from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("", views.index, name="index"),
    path("home1", views.home1, name="home1"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signup1", views.signup1, name="signup1"),
    path("signin1", views.signin1, name="signin1"),
    path("reg", views.reg, name="reg"),
    path("reg1", views.reg1, name="reg1"),
    path("login", views.login, name="login"),
    path("login1", views.login1, name="login1"),
    path("logout", views.logout, name="logout"),
    path("logout1", views.logout1, name="logout1"),
    path("sub", views.sub, name="sub"),
    path("assignment", views.assignment, name="assignment"),
    path("assignmentT", views.assignmentT, name="assignmentT"),
    path("test", views.test, name="test"),
    path("testT", views.testT, name="testT"),
    path("meeting", views.meeting, name="meeting"),
    path("meeting1", views.meeting1, name="meeting1"),
    path("tes", views.tes, name="tes"),
    path("assign", views.assign, name="assign"),
]
