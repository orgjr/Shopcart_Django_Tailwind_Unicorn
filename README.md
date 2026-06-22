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
docker compose -f compose.yaml up --build -d
```

## Running with Django

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py populate
python manage.py runserver
```

Application available at:

```text
http://localhost:8000
```

## Automated Tests

The project includes a comprehensive automated test suite to ensure the reliability and integrity of the application's core functionality.

### Product Model Tests

The `Product` model is covered by tests that validate:

- Create, Read, Update, and Delete (CRUD) operations
- Field validation rules (e.g., negative prices and maximum name length)
- Decimal precision handling for product prices
- Correct string representation of model instances

### Cart Model Tests

The `Cart` model is covered by tests that validate:

- Create, Read, Update, and Delete (CRUD) operations
- Foreign key relationships with `Product` and `User`
- Default quantity values
- Cascade deletion behavior when related products or users are removed
- Updates to calculated fields such as cart subtotals

### User Filtering Function Tests

The `get_users_created_after_date()` function is covered by tests that validate:

- Filtering users created after a given date
- Edge cases involving users created exactly on the reference date
- Proper timezone-aware date handling

### Test Coverage

All tests are implemented in `core/tests.py` and organized into dedicated test classes for each component. The suite currently contains **16 passing tests**, providing confidence in the correctness and stability of the application's model operations and business logic.

## Notes

This project was created as a small experiment integrating Django Unicorn with a traditional Django application workflow.
