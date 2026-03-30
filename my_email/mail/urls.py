from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),  # главная страница
    path("sent/", views.sent, name="sent"),  # исходящие
    path("trash/", views.trash, name="trash"),  # корзина
    path("archive/", views.archive, name="archive"),  # архив
    path(
        "email/<int:mail_id>/return_from/", views.return_from, name="return_from"
    ),  # убрать из архива или корзины
    path(
        "email/<int:mail_id>/archive/", views.move_to_archive, name="move_to_archive"
    ),  # в архив
    path(
        "email/<int:mail_id>/trash/", views.move_to_trash, name="move_to_trash"
    ),  # в корзину
    path("mail/<int:mail_id>/", views.mail, name="mail"),  # страница конкретного письма
    path("create_mail/", views.create_mail, name="create_mail"),  # форма создания письма
]
