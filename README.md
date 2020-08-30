# Aviablog_vuelo
Vuelo_v1
Описание: Авиционный блог на подобии хабр хабр, где могут писать все зарегистрированные

истрцкция по настройке
1.1 Выбери текстовый редактор (мне нравится Visual Studio Code)
1.2 Скачать Python
https://www.python.org/downloads/
1.3 Создай папку бро 
1.4 Скачать виртулку
python -m venv virt
запустить  - .\virt\Scripts\activate
1.5 Скачать django. Для этого открыть cmd в папке (создай папку бро) с проектом и набрать команду pip install django и плагины: 
pip install django-summernote
pip install django-ckeditor
pip install django-crispy-forms
pip install South
pip install pytils
pip install django-admin-tools
pip install Pillow
1.6 Создай проект django-admin.py startproject vuelo
1.7 чекни в браузре localhost:8000
1.8 python manage.py makemigrations и python mange.py migrate
1.9 вбей python manage.py migrate и python manage,py createsuperuser. создай супер юзура) я сделал StepCore pas: 1988Scac! и чекни http://localhost:8000/admin/
1.9 python manage,py startapp vuelo

