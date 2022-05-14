[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

# API for Yatube Social Network

API для взаимодействия с социальной сетью [Yatube](https://github.com/thenorden/YaTube-Based_on_function)

## Описание
Данный проект является планомерным развитием социальной сети для публикации дневников и заметок [Yatube](https://github.com/thenorden/YaTube-Based_on_function). В ней пользователь отправлял запросы на сервер, а в ответ получал готовые HTML-шаблоны со всей необходимой информацией и оформлением. Теперь же нашем распоряжении есть полноценное API для этого проекта, разработанное на основе архитектурного стиля REST. Основное отличие от прошлой версии заключается в том, что данные поступают в клиентскую часть в формате JSON, а не в виде HTML-шаблонов, что позволяет использовать API для реализации веб-сервиса типа SPA. Иными словами, [Yatube](https://github.com/thenorden/YaTube-Based_on_function) + API = Универсальность.

## Технологии
- [Python 3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Git](https://github.com/)

## Установка
1. Клонировать репозиторий
```
git clone https://github.com/thenorden/YaTube-Based_on_function
```
2. Создать виртуальное окружение
```
python -m venv venv
```
3. Активировать виртуальное окружение
```
source venv/scripts/activate
```
4. Установить необходимые пакеты для работы приложения из файла зависимостей
```
pip install -r requirements.txt
```

## Примеры взаимодействия с API
Данный проект имеет широкий фунционал и поддерживает все CRUD-методы (Create, Read, Update, Delete) взаимодействия с базой данных. Ниже в качастве примера приведены запросы для взаимодействия с публикациями.

1. Получить список всех публикаций
```
(GET) http://127.0.0.1:8000/api/v1/posts/
```
2. Создать новую публикацию
```
(POST) http://127.0.0.1:8000/api/v1/posts/
```
3. Получить публикацию по id
```
(GET) http://127.0.0.1:8000/api/v1/posts/{id}/
```
4. Обновить публикацию по id
```
(PUT) http://127.0.0.1:8000/api/v1/posts/{id}/
```
5. Частично обновить публикацию по id
```
(PATCH) http://127.0.0.1:8000/api/v1/posts/{id}/
```
6. Удалить публикацию по id
```
 (DELETE) http://127.0.0.1:8000/api/v1/posts/{id}/
```
Полный список всех запросов можно посмотреть по адресу http://127.0.0.1:8000/redoc/ при локально запущенном проекте.
