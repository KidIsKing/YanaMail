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
    is_read = models.BooleanField(default=True, verbose_name="Статус прочтения")

    # Поля для отправки писем между пользователями
    sender_user = models.ForeignKey(
        User,
        related_name="sent_emails",
        verbose_name=("Отправитель(связ.)"),
        on_delete=models.CASCADE,
        null=True
        )
    recipient_user = models.ForeignKey(
        User,
        related_name="received_emails",
        verbose_name=("Получатель(связ.)"),
        on_delete=models.CASCADE,
        null=True
        )

    class Meta:
        verbose_name = "Письма"
        verbose_name_plural = "Письма"  # иначе "Письмаs"

    def __str__(self):
        return f"from {self.sender} to {self.recipient} -> {self.subject}"
