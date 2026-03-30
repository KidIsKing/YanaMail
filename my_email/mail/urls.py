from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),  # главная страница
    path("sent/", views.sent, name="sent"),  # исходящие
    path("trash/", views.trash, name="trash"),  # корзина
    path("archive/", views.archive, name="archive"),  # архив
    path("mail/<int:mail_id>/", views.mail, name="mail"),  # страница конкретного письма
    path("create_mail/", views.create_mail, name="create_mail"),  # форма создания письма
]
