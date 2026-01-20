# 🚰 Drain Blockage Reporting System

A university-level web application built with **Python & Django** that allows citizens to report drain blockages online and enables authorities to track and manage those reports efficiently.

---

## 📌 Project Information

- **Project Title:** Drain Blockage Reporting System
- **Student Name:** মো: খালিদ মাহমুদ
- **ID (Last 4 Digits):** 1508
- **Session:** 2025
- **Section:** 8A
- **Project Type:** University Academic Project

---

## 🎯 Project Objective

The main objective of this project is to provide a simple and efficient platform where users can report drain blockages, upload images, and track the status of their complaints. This system helps improve cleanliness, hygiene, and response time for drainage issues.

---

## 🛠️ Technology Stack

- **Backend:** Python, Django 5.2
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite
- **Authentication:** Django Built-in Authentication System
- **Tools:** VS Code / PyCharm, Git

---

## 👥 User Roles

### 👤 Citizen/User
- Register an account
- Login & Logout
- Submit drain blockage reports
- Upload images (optional)
- View report status

### 🧑‍💼 Admin
- Login via Django Admin Panel
- View all reports
- Update report status (Pending / In Progress / Resolved)
- Delete invalid reports

---

## ✨ Core Features

- Secure user authentication
- Responsive landing page
- Drain blockage reporting form
- Status tracking system
- Admin management panel

---

## 📂 Project Structure

```
draincare/
│
├── manage.py
├── core/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── apps/
│   ├── accounts/
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── home/
│   │   ├── apps.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── reports/
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│
├── static/
│   └── css/
│       └── style.css
│       └── bootstrap.css
│   └── js/
│       └── main.js
│       └── bootstrap.bundle.js
├── templates/
│   └── base.html
│   └── home.html
│   └── login.html
│   └── register.html
│   └── report_form.html
│   └── report_list.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Project
```bash
git clone <---- YOUR-CLONE-URL -->
cd draincare
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment
**Windows (CMD):**
```bash
venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```bash
pip install django
```

### 5️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run Server
```bash
python manage.py runserver
```

Open browser:
```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Settings

```python
LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/reports/my-reports/'
LOGOUT_REDIRECT_URL = '/user/login/'
```

---

## 🧠 Key Learning Outcomes

- Django MVC architecture
- User authentication & authorization
- CRUD operations
- Form handling & validation
- Error handling (MultiValueDictKeyError fix)
- Responsive UI with Bootstrap

---

## 🎤 Viva Explanation (Summary)

> This system allows users to report drain blockages online. The backend is developed using Django, which manages authentication, database operations, and security. The frontend is responsive and user-friendly, built with Bootstrap.

---

## 🚀 Future Improvements

- Google Map integration
- Email notifications
- REST API with DRF
- Mobile app version
- Role-based permission system

---

## 📜 License

This project is created for **educational purposes only**.

---

## 🙏 Acknowledgement

I would like to thank my teachers and university for their guidance and support throughout this project.

---

**Thank You**

