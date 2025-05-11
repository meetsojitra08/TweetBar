# TweetBar 🐦

**TweetBar** is a Django-based web application designed to manage and display tweet-like posts with media content. It supports image uploads, organized media storage, and an admin panel for content management. This project is ideal for learning Django fundamentals, including models, views, templates, and media handling.

---

## 🧰 Features

- Post tweet-like messages with image uploads
- Media file handling via Django’s file system
- Admin panel for managing content
- Organized project structure
- SQLite for easy development setup
- Clean and minimal frontend

---

## 📁 Project Structure

```
TweetBar/
├── tweet/                  # Django app containing views, models, URLs
├── twitterdjango/          # Main project settings
├── media/                  # Uploaded images and tweet media
├── static/                 # Static files (CSS, JS, etc.)
├── db.sqlite3              # SQLite database
├── manage.py               # Django management utility
├── requirements.txt        # Python dependencies
└── venv/                   # Virtual environment (optional)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/TweetBar.git
cd TweetBar/TweetBar
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`

---

## 🔐 Admin Panel

Login at: `http://127.0.0.1:8000/admin/`  
Use your superuser credentials to manage tweets and media content.

---

## 🖼️ Media Handling

Uploaded media (like tweet images) are stored in the `media/` directory. Django handles media files during development via appropriate URL configurations in `urls.py`.

---

## ✅ Requirements

- Python 3.8 or above
- Django 4.x or compatible
- Other packages listed in `requirements.txt`

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## 🤝 Contribution

Feel free to fork the repo, submit issues, or open pull requests for improvements.

---

## 📬 Contact

For suggestions, issues, or collaboration:
- GitHub: [meetsojitra08](https://github.com/meetsojitra08)
- Email: meetsojitra314@gmail.com
