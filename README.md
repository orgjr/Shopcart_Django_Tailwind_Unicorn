# Django Shopping Cart with Django Unicorn

A modern, interactive shopping cart application built with Django and Django Unicorn, featuring user authentication and real-time cart updates.

## Features

- **User Authentication**

  - User registration and login/logout
  - Protected routes for authenticated users
  - Personalized user greeting

- **Product Management**

  - Product listing with names and prices
  - Dynamic product display

- **Shopping Cart**
  - Add/remove items
  - Update quantities
  - Real-time cart updates without page refresh
  - Automatic total calculation

## Tech Stack

- **Backend**: Django 6.0
- **Frontend**:
  - HTML, JavaScript
  - Tailwind CSS for styling
- **Real-time Updates**: Django Unicorn
- **Database**: SQLite (default)
- **Authentication**: Django's built-in auth system

## Installation

1. Clone the repository:

   ```bash
   git clone [your-repository-url]
   cd shop_cart_unicorn
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`

## Project Structure

```
shop_cart_unicorn/
├── core/                    # Main application
│   ├── components/          # Django Unicorn components
│   │   └── cart.py          # Cart component logic
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── core/            # Core templates
│   │   └── unicorn/         # Unicorn component templates
│   ├── __init__.py
│   ├── admin.py             # Admin interface config
│   ├── apps.py              # App config
│   ├── models.py            # Database models
│   ├── urls.py              # URL routing
│   └── views.py             # View functions
├── shopcart/                # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI config
├── .gitignore
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## Usage

1. **Browse Products**

   - Visit the home page to view available products
   - No login required to browse

2. **User Authentication**

   - Click "Login" to sign in or register
   - Access protected routes after login

3. **Shopping Cart**
   - Add items to your cart
   - View and manage cart contents
   - Update quantities or remove items
   - See real-time updates without page refresh

## Configuration

### Environment Variables

Create a `.env` file in the project root with your configuration:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### Django Unicorn

The application uses Django Unicorn for real-time updates. The main cart functionality is handled in `core/components/cart.py`.

## License

[MIT License](LICENSE)
