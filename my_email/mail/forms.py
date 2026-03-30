from django import forms

from .models import Mail


class MailForm(forms.ModelForm):
    recipient = forms.CharField(
        label="Кому", max_length=100, help_text="Введите имя пользователя получателя"
    )

    class Meta:
        model = Mail
        fields = ("recipient", "subject", "text")
