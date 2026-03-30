from django.db import models
from django.contrib.auth import get_user_model


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
