<<<<<<< HEAD
Вот версия в совершенно другом стиле оформления — более современном, лаконичном и «продуктовом» (как в хороших репозиториях на GitHub):

```markdown
# TaskFlow Backend

Современный API для управления задачами на FastAPI.

### Возможности

-  Регистрация и авторизация через JWT  
-  Полный CRUD задач  
-  Роли пользователей: **user** и **admin**  
-  Кэширование задач с помощью Redis  

---

### Архитектура

Проект построен по принципам **Clean Architecture** и разделён на чёткие слои:

- **core** — конфигурация, БД, безопасность  
- **models** — SQLAlchemy модели  
- **schemas** — Pydantic схемы валидации  
- **repositories** — работа с данными  
- **services** — бизнес-логика  
- **api** — маршруты и эндпоинты  

![Структура проекта](image-1.png)

---

### Запуск

```bash
docker-compose up --build
```

Приложение будет доступно по адресу:  
**http://localhost:8000/docs**

---

### API Эндпоинты

**Авторизация**
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

**Задачи**
- `POST /tasks/` — создать
- `GET /tasks/` — список
- `GET /tasks/{task_id}` — получить
- `PATCH /tasks/{task_id}` — обновить
- `DELETE /tasks/{task_id}` — удалить

**Админ**
- `GET /admin/users` — список пользователей

---

### Скриншоты

**Управление задачами**  
![Tasks](image-2.png)

**Админ-панель**  
![Admin](image-2.png)

**Документация и интерфейс**  
![Swagger](image-3.png)
![Swagger](image-4.png)
![Swagger](image-5.png)
![Swagger](image-6.png)
![Swagger](image-7.png)
![Swagger](image-8.png)
![Swagger](image-9.png)
![Swagger](image-10.png)
![Swagger](image-11.png)
![Swagger](image-12.png)
![Swagger](image-13.png)

---

### Docker

Состоит из двух сервисов:
- **backend** — FastAPI (uvicorn)
- **redis** — кэш

<img width="1216" height="45" alt="Docker Compose" src="https://github.com/user-attachments/assets/331713bf-0174-4f36-84e7-dc1a5adc5675" />

---

### Реализовано

- Разбиение монолита на модульную структуру  
- Чистая архитектура  
- JWT-аутентификация  
- Redis-кэширование  
- Запуск через Docker Compose  
- Автогенерируемая Swagger-документация  

---
=======
# Task Tracker API

Проект в процессе рефакторинга из монолита в чистую структуру.
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
