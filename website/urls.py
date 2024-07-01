from django.urls import path
from . import views
app_name="website"
urlpatterns =[
    path('',views.home,name="home"),
    #path("login/",views.loginUser,name="loginUser"),
    path("logout/",views.logoutUser,name="logoutUser"),
    path("register/",views.registerUser,name="register"),
    path("record/<int:pk>",views.record,name="record"),
    path("delete/<int:pk>",views.deleteRecord,name="deleteRecord"),
    path("addrecord",views.addRecord,name="addRecord"),
    path("upadeterecord/<int:pk>",views.updateRecord,name="updateRecord")

]   