from django.db import models
from django.contrib.auth import get_user_model


STATUSES = (
    "inbox",  # входящие
    "sent",  # исходящие
    "trash",  # корзина
    "archive"  # архив
)

User = get_user_model()


class Mail(models.Model):
    sender = models.CharField(max_length=100, verbose_name="Отправитель")
    recipient = models.CharField(max_length=100, verbose_name="Получатель")
    subject = models.CharField(max_length=100, verbose_name="Тема")
    text = models.TextField(verbose_name="Текст письма")
    created_at = models.DateTimeField(
        auto_now_add=True,  # сохранить дату создания
        verbose_name="Дата создания"
        )
    status = models.SlugField(
        max_length=50,
        default=STATUSES[1],  # по умолчанию - "sent"
        verbose_name="Статус"
        )
    old_status = models.SlugField(
        max_length=50,
        default="",  # начальное значение, которое будет перезаписано позже
        verbose_name="Начальный статус"
        )

    class Meta:
        verbose_name = "Письма"
        verbose_name_plural = "Письма"  # иначе "Письмаs"

    def __str__(self):
        return f"from {self.sender} to {self.recipient} -> {self.subject}"
