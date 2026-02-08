#Задание 2 (Средний уровень)
#Реализация стандартной системы аутентификации

#1.Настрой Django-приложение с использованием стандартной модели пользователя.
#2.Добавь страницу регистрации (register.html) с формой UserCreationForm.
#3.Настрой автоматический редирект после успешной регистрации на страницу входа.
#4.Реализуйте страницу профиля (profile.html), доступную только авторизованным пользователям (используйте LoginRequiredMixin).
#5.Отправь архив с проектом или файлы views.py, urls.py и HTML-шаблоны.


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autenyific_polzovatel.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
