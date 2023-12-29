from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path("mark_as_done/<int:pk>",views.mark_as_done,name="mark_as_done"),
    path("delete/<int:pk>",views.delete,name="delete"),
    path("edittask/<int:pk>",views.edittask,name="edittaskexit"),
    
]