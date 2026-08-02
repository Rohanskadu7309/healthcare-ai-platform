# 🏥 Healthcare AI Platform

A production-ready backend Healthcare Management Platform built using **Django** and **Django REST Framework**, featuring secure REST APIs, AI-powered healthcare analytics, disease prediction, medical report summarization, and modern backend architecture.

---

# 📌 Project Status

🚧 **Currently under active development.**

The project is being developed module-by-module following industry-standard software development practices including feature branching, clean architecture, API documentation, testing, and production-ready coding standards.

---

# 🚀 Features Implemented

## Authentication

- ✅ Custom User Model (Email Authentication)
- ✅ User Registration
- ✅ User Login
- ✅ JWT Authentication
- ✅ Refresh Token
- ✅ Logout (JWT Token Blacklisting)
- ✅ Get Profile
- ✅ Update Profile
- ✅ Change Password

---

# 🚧 Upcoming Features

## Authentication

- ⏳ Forgot Password
- ⏳ Reset Password
- ⏳ Email Verification
- ⏳ Two-Factor Authentication (TOTP)

## Authorization

- ⏳ Role-Based Access Control (RBAC)
- ⏳ Roles & Permissions

---

# 🎯 Project Objectives

- Build secure REST APIs using Django REST Framework.
- Manage patients, doctors, appointments, and medical records.
- Analyze healthcare data using Pandas and NumPy.
- Predict disease risks using Machine Learning.
- Generate AI-powered medical summaries using LLMs.
- Provide an enhanced Django Admin experience.
- Follow clean architecture and production-ready development practices.

---

# 🚀 Tech Stack

## Backend

- Python 3.12.10
- Django 6.0.3
- Django REST Framework
- PostgreSQL 17

## Authentication

- JWT Authentication (Simple JWT)
- Token Blacklisting

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn
- Joblib

## AI Integration

- OpenAI API
- Google Gemini API
- LangChain

## Background Tasks

- Celery
- Redis

## Documentation

- Swagger UI (drf-spectacular)
- ReDoc
- OpenAPI Schema

## Reports

- ReportLab
- OpenPyXL

## Version Control

- Git
- GitHub

---

# 📂 Planned Modules

## 🔐 Authentication

- ✅ Register
- ✅ Login
- ✅ JWT Authentication
- ✅ Refresh Token
- ✅ Logout
- ✅ Get Profile
- ✅ Update Profile
- ✅ Change Password
- ⏳ Forgot Password
- ⏳ Reset Password
- ⏳ Email Verification
- ⏳ Two-Factor Authentication (TOTP)

---

## 👥 Authorization

- ⏳ Role-Based Access Control (RBAC)
- ⏳ Roles
- ⏳ Permissions

---

## 🏥 Healthcare Management

- ⏳ Patient Management
- ⏳ Doctor Management
- ⏳ Appointment Scheduling
- ⏳ Medical Records
- ⏳ Prescription Management

---

## 📊 Healthcare Analytics

- ⏳ Dashboard APIs
- ⏳ CSV Upload
- ⏳ Data Processing
- ⏳ Healthcare Analytics APIs

---

## 🤖 Artificial Intelligence

- ⏳ Disease Risk Prediction
- ⏳ AI Medical Report Summary
- ⏳ AI Healthcare Assistant

---

## 📄 Reports

- ⏳ PDF Reports
- ⏳ Excel Reports

---

## ⚙ Infrastructure

- ⏳ Celery
- ⏳ Redis
- ⏳ Docker
- ⏳ Automated Testing
- ⏳ CI/CD Pipeline

---

# 📁 Project Structure

```text
healthcare-ai-platform/

├── accounts/
├── api/
├── common/
├── config/
├── logs/
├── media/
├── static/
├── .env
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

# 📖 API Documentation

Run the development server:

```bash
python manage.py runserver
```

Available API documentation:

### Swagger UI

```
http://127.0.0.1:8000/api/docs/
```

### ReDoc

```
http://127.0.0.1:8000/api/redoc/
```

### OpenAPI Schema

```
http://127.0.0.1:8000/api/schema/
```

---

# 🌳 Git Workflow

```text
master
   │
develop
   │
feature/*
```

Development workflow:

- Create a feature branch from `develop`
- Complete one feature
- Test using Swagger and Postman
- Merge into `develop`
- Merge stable releases into `master`

---

# 📅 Development Roadmap

## ✅ Phase 1 — Project Setup

- Project Initialization
- Virtual Environment
- PostgreSQL Configuration
- Django REST Framework
- Swagger Documentation
- Custom User Model

---

## 🚧 Phase 2 — Authentication

- ✅ Register
- ✅ Login
- ✅ JWT Authentication
- ✅ Refresh Token
- ✅ Logout
- ✅ Get Profile
- ✅ Update Profile
- ✅ Change Password
- ⏳ Forgot Password
- ⏳ Reset Password
- ⏳ Email Verification
- ⏳ Two-Factor Authentication
- ⏳ Role-Based Access Control (RBAC)

---

## ⏳ Phase 3 — Healthcare Modules

- Patient Management
- Doctor Management
- Appointment Scheduling
- Medical Records
- Prescription Management

---

## ⏳ Phase 4 — Healthcare Analytics

- Dashboard APIs
- CSV Import
- Healthcare Reports
- Data Visualization

---

## ⏳ Phase 5 — Artificial Intelligence

- Disease Prediction API
- AI Medical Report Summary
- AI Healthcare Assistant

---

## ⏳ Phase 6 — Deployment

- Celery
- Redis
- Docker
- Automated Testing
- CI/CD
- Cloud Deployment

---

# 🕒 Time Zone

All timestamps are stored in **UTC** and displayed in **Indian Standard Time (IST)**.

```
Time Zone: Asia/Kolkata (UTC +05:30)
```

---

# 👨‍💻 Author

**Rohan Kadu**

Backend Developer | Python | Django | Django REST Framework

---

# 📄 License

This project is licensed under the MIT License.