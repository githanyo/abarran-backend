# Abarran Tree Project – Farmer Registration System (Backend)

This project is a backend system for the **Abarran Tree Project**, designed to register, manage, and administer farmer data securely.  
It provides a RESTful API used by an admin dashboard and a public farmer registration form.

---

## Features

- Farmer registration (public)
- Admin authentication (JWT)
- Role-based access control (admin only)
- Farmer list with pagination & search
- Farmer detail view
- Edit and delete farmer records
- Secure production deployment

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (development), easily extendable to PostgreSQL
- **Deployment:** Render
- **Security:** Environment variables, role-based permissions

---
## Project Structure

abarran-backend/
├── abarran_backend/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── farmers/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── permissions.py
│ └── urls.py
├── manage.py
└── requirements.txt

---

## Authentication

This project uses **JWT authentication**.

### Obtain token


## 📂 Project Structure

