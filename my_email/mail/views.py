from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Mail, User
from .forms import MailForm


@login_required
def index(request):
    """Главная страница со списком входящих писем."""
    template_name = "mail/index.html"
    mails_list = Mail.objects.filter(
        recipient_user=request.user,
        status="inbox"
        ).order_by("-created_at")
    context = {"mails_list": mails_list}
    return render(request, template_name, context)


@login_required
def sent(request):
    """Cтраница со списком отправленных писем."""
    template_name = "mail/sent.html"
    mails_sent_list = Mail.objects.filter(
        sender_user=request.user,
        status="sent"
        ).order_by("-created_at")
    context = {"mails_sent_list": mails_sent_list}
    return render(request, template_name, context)


@login_required
def trash(request):
    """Cтраница с корзиной."""
    template_name = "mail/trash.html"
    mails_trash_list = Mail.objects.filter(
        recipient_user=request.user,
        status="trash"
        ).order_by("-created_at")
    context = {"mails_trash_list": mails_trash_list}
    return render(request, template_name, context)


@login_required
def archive(request):
    """Cтраница с архивом."""
    template_name = "mail/archive.html"
    mails_archive_list = Mail.objects.filter(
        recipient_user=request.user,
        status="archive"
        ).order_by("-created_at")
    context = {"mails_archive_list": mails_archive_list}
    return render(request, template_name, context)


def mail(request, mail_id):
    """Страница конкретного письма."""
    template_name = "mail/mail.html"
    mail = get_object_or_404(Mail, pk=mail_id)
    context = {"mail": mail}
    return render(request, template_name, context)


def create_mail(request):
    """Страница с формой создания письма."""
    template_name = "mail/create_mail.html"
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            recipient_username = form.cleaned_data["recipient"]
            recipient_user = User.objects.get(username=recipient_username)

            # Письмо для отправителя (для вкладки "Исходящие")
            sent_mail = Mail(
                sender=request.user.username,
                recipient=recipient_username,
                subject=form.cleaned_data["subject"],
                text=form.cleaned_data["text"],
                status="sent",
                is_read=True,
                sender_user=request.user,
                recipient_user=recipient_user
            )
            sent_mail.save()

            # Письмо для получателя (для вкладки "Входящие")
            received_email = Mail(
                sender=request.user.username,
                recipient=recipient_username,
                subject=form.cleaned_data["subject"],
                text=form.cleaned_data["text"],
                status="inbox",
                is_read=False,
                sender_user=request.user,
                recipient_user=recipient_user
            )
            received_email.save()
            return redirect("index")
    else:
        form = MailForm()
    context = {"form": form}
    return render(request, template_name, context)


def return_from(request, mail_id):
    """Возвращение из архива или корзины."""
    mail = get_object_or_404(Mail, pk=mail_id)
    mail.status = mail.old_status  # восстанавливаем начальный статус
    mail.save()
    return redirect("index")


def move_to_archive(request, mail_id):
    """Отправка в архив."""
    mail = get_object_or_404(Mail, pk=mail_id)
    mail.old_status = mail.status  # сначала сохраняем текущий статус
    mail.status = "archive"  # меняем статус на архив
    mail.save()
    return redirect("index")


def move_to_trash(request, mail_id):
    """Отправка в корзину."""
    mail = get_object_or_404(Mail, pk=mail_id)
    mail.old_status = mail.status  # сначала сохраняем текущий статус
    mail.status = "trash"  # меняем статус на корзину
    mail.save()
    return redirect("index")


def delete(request, mail_id):
    """Удаление (из корзины)."""
    mail = get_object_or_404(Mail, pk=mail_id)
    mail.delete()
    return redirect("index")
