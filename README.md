# 👤 Personal Information Manager

![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A secure, Django-based web application for storing and managing personal information, documents, and sensitive data in one centralized location.

---

## ✨ Features

- 🔐 **Secure Storage** - Encrypt and store personal information safely
- 👤 **Profile Management** - Manage personal details, contacts, and identities
- 📄 **Document Vault** - Store and organize important documents
- 🏷️ **Categorization** - Organize info by categories and tags
- 🔍 **Quick Search** - Find information instantly
- 🛡️ **User Authentication** - Secure login and access control
- 📱 **Responsive Design** - Access from any device
- 🔔 **Reminders** - Alerts for document expirations and renewals

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 4.x |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite / PostgreSQL |
| Authentication | Django Auth System |
| Security | Django Security Middleware |

---

## ⚡ Installation

### Prerequisites

- Python 3.10+
- pip or pipenv
- Git

### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/faridi-nayunda/personal-info-manager.git
cd personal-info-manager

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver

# 8. Open browser at http://127.0.0.1:8000
