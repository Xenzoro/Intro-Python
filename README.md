# CS50W Django Projects

This repository contains Django web applications developed while learning CS50W (CS50's Web Programming with Python and JavaScript). The projects demonstrate core Django concepts including models, views, templates, forms, authentication, and database relationships.

## 📚 About

These projects are based on material from **Harvard's CS50W course**. This repository includes my working implementations along with PDF notes taken on my iPad during the learning process.

## 🗂️ Projects

### 1. Airline Flight Management System (`airline/`)

A comprehensive flight booking system that demonstrates Django's ORM, many-to-many relationships, and the admin interface.

**Features:**
- Airport and flight management with foreign key relationships
- Passenger booking system with many-to-many relationships
- User authentication system (login/logout)
- Flight detail views with passenger lists
- Book passengers on flights

**Key Concepts:**
- Django Models (ForeignKey, ManyToManyField)
- Cascade deletion and related_name
- Django Admin interface
- User authentication and sessions
- Template inheritance and URL routing

---

### 🔑 Test Users

> **Important:** Use these credentials to test the authentication system

| Username | Password |
|----------|----------|
| **harry** | `boogers!` |
| **ron** | `notBoogers!` |

Access the login page at: `http://localhost:8000/users/login`

---

**Models:**
- `Airport`: Airport code and city
- `Flight`: Origin, destination, duration with foreign keys to Airport
- `Passenger`: First name, last name, and many-to-many relationship with flights

### 2. Hello World App (`lecture3/hello/`)

A simple introductory Django application demonstrating basic routing and template rendering.

**Features:**
- Basic HTTP responses
- Dynamic URL parameters
- Template rendering with context variables
- Personalized greeting pages

**Key Concepts:**
- Django views and HttpResponse
- URL patterns with parameters
- Template rendering
- Context dictionaries

### 3. New Year Checker (`lecture3/newyear/`)

A simple application that checks if it's New Year's Day.

**Features:**
- Date-based conditional rendering
- Static file serving (CSS)
- Template logic

**Key Concepts:**
- Python datetime module
- Template conditionals
- Static files in Django

### 4. Task Management (`lecture3/tasks/`)

A task list application with session-based storage.

**Features:**
- Add new tasks via forms
- View all tasks in a list
- Session-based task storage (persists across page loads)
- Form validation

**Key Concepts:**
- Django Forms
- Session management
- Form handling (GET/POST)
- HttpResponseRedirect
- CSRF protection

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Django 4.2.11
- SQLite (included with Python)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Intro-Python
```

2. Install Django (if not already installed):
```bash
pip install django
```

### Running the Projects

#### Airline App

```bash
cd airline
python manage.py migrate
python manage.py runserver
```

Visit `http://localhost:8000/flights/` to view flights.

**Creating Test Data:**

```bash
python manage.py shell
```

```python
from flights.models import Airport, Flight, Passenger

# Create airports
jfk = Airport(code="JFK", city="New York")
jfk.save()

lhr = Airport(code="LHR", city="London")
lhr.save()

# Create a flight
flight = Flight(origin=jfk, destination=lhr, duration=415)
flight.save()

# Create passengers
harry = Passenger(first="Harry", last="Potter")
harry.save()

ron = Passenger(first="Ron", last="Weasley")
ron.save()
```

#### Lecture3 Apps (Hello, Tasks, New Year)

```bash
cd lecture3
python manage.py migrate
python manage.py runserver
```

Access the apps at:
- Hello: `http://localhost:8000/hello/`
- Tasks: `http://localhost:8000/tasks/`
- New Year: `http://localhost:8000/newyear/` (not included in current setup)

## 🎓 Learning Outcomes

Through these projects, I learned:

- **Django Framework Fundamentals**
  - Model-View-Template (MVT) architecture
  - URL routing and view functions
  - Template engine and inheritance
  
- **Database Design**
  - ORM (Object-Relational Mapping)
  - Foreign keys and cascade deletion
  - Many-to-many relationships
  - Database migrations
  
- **Web Development Concepts**
  - HTTP request/response cycle
  - Form handling and validation
  - CSRF protection
  - Session management
  - User authentication
  
- **Django Admin**
  - Registering models
  - Customizing admin interface
  - Data management through admin panel

## 📝 Notes

This repository includes **handwritten notes taken on my iPad** during the CS50W course. These notes complement the code and provide additional context and explanations of the concepts covered.

### 📖 Available Notes

- **[CS50 Django & Python](notes/C50%20Django-py.png)** - Comprehensive notes on Django framework and Python concepts
- **[CS50 Python](notes/Cs50%20python-py.png)** - Core Python programming notes
- **[CS50 SQL](notes/CS50%20SQL.png)** - Database and SQL concepts



## 🛠️ Django Management Commands

Useful commands for working with these projects:

```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create a superuser for admin panel
python manage.py createsuperuser

# Open Django shell for testing
python manage.py shell

# Start development server
python manage.py runserver
```

## 📂 Project Structure

```
Intro-Python/
├── airline/              # Flight management system
│   ├── flights/         # Flights app
│   ├── users/          # User authentication app
│   └── db.sqlite3      # Database
├── lecture3/            # Learning projects
│   ├── hello/          # Hello world app
│   ├── tasks/          # Task management app
│   └── newyear/        # New Year checker app
├── notes/               # 📝 iPad notes from CS50W
│   ├── C50 Django-py.png
│   ├── Cs50 python-py.png
│   └── CS50 SQL.png
└── README.md           # This file
```

## 🔐 Security Note

This is a learning project. The SECRET_KEY and DEBUG settings are not suitable for production. Always:
- Use environment variables for sensitive data
- Set DEBUG = False in production
- Use strong, unique SECRET_KEY values
- Implement proper authentication and authorization

## 📚 Resources

- [CS50W Course](https://cs50.harvard.edu/web/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

## 👤 Author

Created as part of CS50W coursework.

## 📄 License

This project is for educational purposes as part of CS50W.

---

*Note: This repository represents my journey learning web development with Django through Harvard's CS50W course.*

