from django import forms

from .models import Mail, User


class MailForm(forms.ModelForm):
    """Форма создания письма."""
    recipient = forms.ModelChoiceField(
        label="Кому",
        queryset=User.objects.all(),
        to_field_name="username",
        help_text="Введите имя пользователя получателя"
    )

    class Meta:
        model = Mail
        fields = ("recipient", "subject", "text")
