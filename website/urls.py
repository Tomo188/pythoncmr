from django.urls import path
from . import views
app_name="website"
urlpatterns =[
    path('',views.home,name="home"),
    #path("login/",views.loginUser,name="loginUser"),
    path("logout/",views.logoutUser,name="logoutUser"),
    path("register/",views.registerUser,name="register")
]   