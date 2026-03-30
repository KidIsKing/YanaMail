from django.shortcuts import render, redirect, get_object_or_404

from .models import Mail
from .forms import MailForm


def index(request):
    """Главная страница со списком входящих писем."""
    template_name = "mail/index.html"
    mails_list = Mail.objects.filter(status="inbox").order_by("-created_at")
    context = {"mails_list": mails_list}
    return render(request, template_name, context)


def sent(request):
    """Cтраница со списком отправленных писем."""
    template_name = "mail/sent.html"
    mails_sent_list = Mail.objects.filter(status="sent").order_by("-created_at")
    context = {"mails_sent_list": mails_sent_list}
    return render(request, template_name, context)


def trash(request):
    """Cтраница с корзиной."""
    template_name = "mail/trash.html"
    mails_trash_list = Mail.objects.filter(status="trash").order_by("-created_at")
    context = {"mails_trash_list": mails_trash_list}
    return render(request, template_name, context)


def archive(request):
    """Cтраница с архивом."""
    template_name = "mail/archive.html"
    mails_archive_list = Mail.objects.filter(status="archive").order_by("-created_at")
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
            form.save()
            return redirect("index")
    else:
        form = MailForm()
    context = {"form": form}
    return render(request, template_name, context)
