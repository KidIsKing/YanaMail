from django.shortcuts import render, redirect

from .models import Mail
from .forms import MailForm


def index(request):
    """Главная страница со списком писем."""
    template_name = "mail/index.html"
    mails_list = Mail.objects.all()
    context = {"mails_list": mails_list}
    return render(request, template_name, context)


def create_mail(request):
    """Главная страница со списком писем."""
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
