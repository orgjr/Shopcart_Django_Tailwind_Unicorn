# Django Shopping Cart with Django Unicorn

Simple shopping cart application built with Django and Django Unicorn to explore reactive UI patterns without writing custom JavaScript.

## Stack

- Django
- Django Unicorn
- Tailwind CSS
- SQLite
- Docker

## Features

- User authentication
- Dynamic cart updates
- Quantity management
- Real-time UI interactions with Django Unicorn

## Running with Docker

```bash
docker compose up --build
```

Application available at:

```text
http://localhost:8000
```

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## Notes

This project was created as a small experiment integrating Django Unicorn with a traditional Django application workflow.
