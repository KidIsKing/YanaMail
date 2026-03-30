from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),  # главная страница
    path("create_mail/", views.create_mail, name="create_mail"),
]
