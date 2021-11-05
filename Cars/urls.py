from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home),
    path('<int:id>',views.ChangeImage,name="change_image"),
]