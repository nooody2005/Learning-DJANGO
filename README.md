# 🐍 Django Learning Journey & FoodApp

A hands-on Django learning journey based on the Udemy course **[Django Masterclass: Build 9 Real World Django Projects](https://www.udemy.com/course/django-course/)**.

This repository documents my progress in learning Django, exploring its core concepts, and applying them through practical development.

It includes my first Django project, **FoodApp**, where I practiced building a complete web application with user authentication, CRUD operations, database management, caching, pagination, and REST API development.

---

## 🚀 About This Repository

The main goal of this repository is to build a solid foundation in Django and understand how its different components work together to develop dynamic web applications.

Throughout this journey, I explored:

- Django project and app structure.
- Models, Views, URLs, and Templates.
- Database operations and migrations.
- Forms and ModelForms.
- User authentication and profile management.
- CRUD operations.
- Django REST Framework.
- Serializers and API development.
- Custom permissions and middleware.
- Pagination and caching.
- Custom model managers and template tags.

---

## 🍔 FoodApp — First Practical Project

FoodApp is the first practical application I developed during this learning journey.

It helped me apply Django concepts in a real project structure and understand how the backend handles user requests, database operations, authentication, and API responses.

### ✨ Features

#### 👤 User Authentication & Management
- User registration.
- User login and logout.
- User profile management.
- Authentication-based access control.

#### 📦 Items Management
- Create, retrieve, update, and delete items.
- Manage item data using Django models.
- Handle database operations through Django ORM.

#### 📄 Pagination & Caching
- Implement pagination to organize and display data.
- Explore caching to improve application performance.

#### 🔌 REST API Development
- Build REST APIs using Django REST Framework.
- Use serializers to convert model data into API responses.
- Implement API views and URL routing.
- Apply custom permissions.
- Explore request handling and API access control.

---

## 🛠️ Technologies & Tools

| Technology | Usage |
|---|---|
| Python | Main programming language |
| Django | Backend web framework |
| Django REST Framework | REST API development |
| SQLite | Development database |
| HTML | Templates and page structure |
| CSS | Styling |
| JavaScript | Frontend interactions |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
Django-Learning-Journey-and-Projects/
│
├── myapp/
│   ├── migrations/
│   ├── static/
│   │   └── myapp/
│   ├── templates/
│   │   └── myapp/
│   ├── templatetags/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── managers.py
│   ├── middleware.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── profile.html
│   │       └── register.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── pictures/
├── items.json
├── manage.py
└── .gitignore
```

---

## 📚 What I Learned

This journey helped me understand how Django works beyond the basics.

### 1. Django Fundamentals
- Creating projects and applications.
- Understanding Django's MVT architecture.
- Connecting URLs, Views, Models, and Templates.
- Working with Django settings and static files.

### 2. Database & ORM
- Creating and managing database models.
- Performing CRUD operations using Django ORM.
- Running database migrations.
- Working with model relationships.
- Using custom model managers.

### 3. Forms & Authentication
- Creating Django Forms and ModelForms.
- Handling GET and POST requests.
- Implementing user registration and authentication.
- Managing user profiles and protected pages.

### 4. Advanced Django Concepts
- Custom middleware.
- Custom template tags.
- Pagination.
- Caching.
- Custom permissions.

### 5. Django REST Framework
- Understanding serializers.
- Building REST API endpoints.
- Handling API requests and responses.
- Applying permissions to API views.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/nooody2005/Django-Learning-Journey-and-Projects.git
```

### 2. Navigate to the Project Directory

```bash
cd Django-Learning-Journey-and-Projects
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install django djangorestframework
```

> If a `requirements.txt` file is available, install the project dependencies using `pip install -r requirements.txt` instead.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🎯 Learning Goals

Through this repository, I aimed to:

- Build a strong foundation in Django development.
- Understand how Django handles requests and responses.
- Work confidently with databases and Django ORM.
- Implement authentication and authorization.
- Build REST APIs using Django REST Framework.
- Explore performance optimization techniques.
- Gain practical experience by building a complete application.

---

## 🌱 What's Next?

This repository is part of my continuous journey toward becoming a **Python Backend Developer**.

My next steps include exploring more advanced Django concepts, building additional real-world projects, and improving my backend development skills.

---

## 👩‍💻 Author

**Nada Hashem**

- GitHub: [@nooody2005](https://github.com/nooody2005)
- Learning Track: Python Backend Development
- Course: [Django Masterclass — Build 9 Real World Django Projects](https://www.udemy.com/course/django-course/)

---

⭐ This repository represents an important step in my journey from learning Django fundamentals to building practical backend applications.
