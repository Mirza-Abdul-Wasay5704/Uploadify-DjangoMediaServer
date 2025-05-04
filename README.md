# CN-Project: Simple HTTP Web Server

A modern Django-based web application that allows multiple users to register, log in, and manage their own media content (images, videos, audio). The project features a user-friendly interface for uploading, viewing, and managing media files, with robust authentication and authorization.

---

## 🚀 Features

- **User Registration & Authentication**
  - Secure sign up, login, logout, and profile management
- **Media Management**
  - Upload images, videos, and audio files
  - View, detail, and delete your own media
  - Public/private media visibility
- **Dashboard**
  - Personalized dashboard for each user
- **Responsive UI**
  - Clean, modern templates for all major pages
- **Django Admin**
  - Manage users and media files via Django admin panel

---

## 🗂️ Project Structure

```
web_server_project/
├── db.sqlite3                # SQLite database
├── manage.py                 # Django project manager
├── http_server/              # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── users/                    # User management app
│   ├── views.py
│   ├── forms.py
│   ├── templates/users/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   └── ...
├── media_uploads/            # Media management app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/media_uploads/
│   │   ├── dashboard.html
│   │   ├── upload_media.html
│   │   ├── home.html
│   │   ├── media_detail.html
│   │   └── delete_media.html
│   └── ...
├── templates/base/           # Base templates
│   └── base.html
└── media/                    # Uploaded media files
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CN-Project/web_server_project
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install django
   ```
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
7. **Access the app**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

---

## 📝 Usage Guide

- **Register** for a new account or **log in** with existing credentials
- **Upload media** (image, video, audio) from your dashboard
- **View, detail, and delete** your uploaded media
- **Browse public media** on the home page
- **Manage users and media** via the Django admin panel (`/admin`)

---

## 📸 Screenshots

> _Add screenshots of your app here!_

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](LICENSE) (or specify your license here)
