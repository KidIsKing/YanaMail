from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.contrib import admin
from django.urls import path, include, reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mail.urls')),  # подключаем маршруты mail
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('index'),
        ),
        name='registration',
    ),
]
