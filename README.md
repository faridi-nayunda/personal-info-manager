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
Clone the repository
git clone https://github.com/faridi-nayunda/personal-info-manager.git
cd personal-info-manager

Create virtual environment
python -m venv venv

Activate virtual environment
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Apply database migrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Run development server
python manage.py runserver


Open http://127.0.0.1:8000 in your browser.

---

## 🚀 Usage

1. **Register/Login** - Create an account or sign in securely
2. **Add Personal Info** - Store contact details, addresses, IDs
3. **Upload Documents** - Save passports, certificates, contracts
4. **Organize** - Categorize with custom tags and folders
5. **Search** - Use the search bar to find anything quickly
6. **Set Reminders** - Get alerts for expiring documents

---

## 🔐 Security Features

- Password hashing with Django's PBKDF2 algorithm
- CSRF protection on all forms
- Secure session management
- SQL injection protection
- XSS protection
- Optional: Two-factor authentication (2FA)

---

## 📸 Screenshots

| Dashboard | Profile View | Document Upload |
|-----------|--------------|-----------------|
| screenshots/dashboard.png | screenshots/profile.png | screenshots/upload.png |

---

## 🗂️ Project Structure
personal-info-manager/
├── personal_info/ # Main Django app
│ ├── models.py # Info, Document, Category models
│ ├── views.py # Views for CRUD operations
│ ├── forms.py # Django forms
│ ├── urls.py # URL patterns
│ └── templates/ # HTML templates
├── static/ # CSS, JS, images
├── media/ # User uploaded files
├── templates/ # Base templates
├── manage.py
├── requirements.txt
└── README.md

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

text

### Production Setup

- Set `DEBUG=False`
- Use PostgreSQL database
- Enable HTTPS/SSL
- Configure proper `ALLOWED_HOSTS`
- Set up email backend for notifications

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 Roadmap

- [ ] End-to-end encryption for sensitive data
- [ ] Mobile app (React Native/Flutter)
- [ ] Biometric authentication
- [ ] Cloud backup integration (Google Drive/Dropbox)
- [ ] Document OCR and text extraction
- [ ] Emergency contact access
- [ ] Data export/import functionality

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**Faridi Nayunda**

- GitHub: [@faridi-nayunda](https://github.com/faridi-nayunda)
- Project Link: [https://github.com/faridi-nayunda/personal-info-manager](https://github.com/faridi-nayunda/personal-info-manager)

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Cryptography Library](https://cryptography.io/)
- [Bootstrap](https://getbootstrap.com/) / [TailwindCSS](https://tailwindcss.com/)

---

<div align="center">
⭐ Star this repository if you found it helpful! ⭐
</div>
