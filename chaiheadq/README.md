# ChaiHeadQ - Django Tweet Application 🐦☕

A modern, responsive tweet posting web application built with **Django** framework. Users can create, edit, delete tweets, and upload photos with a beautiful, modern UI featuring dark mode support.

## ✨ Features

- 🔐 **User Authentication** - Secure login, logout, and registration system
- 📝 **Tweet Management** - Create, edit, and delete tweets with rich text
- 📸 **Photo Upload** - Upload and display images with tweets
- 🎨 **Modern UI** - Beautiful, responsive design with Bootstrap 5
- 🌙 **Dark Mode** - Toggle between light and dark themes
- 📱 **Mobile Responsive** - Optimized for all device sizes
- 🔧 **Admin Panel** - Full Django admin interface for content management
- 🛡️ **Security** - Environment variables for sensitive data

## 🚀 Tech Stack

- **Backend:** Django 4.2.7 (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** SQLite3 (Development)
- **Authentication:** Django's built-in auth system
- **File Storage:** Local media storage
- **Environment:** Python-dotenv for configuration management

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chaiheadq.git
cd chaiheadq
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

1. Copy the environment template:
```bash
cp env_template.txt .env
```

2. Edit `.env` file with your configuration:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Database Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python create_superuser.py
```

### 6. Run the Development Server

```bash
python manage.py runserver 8001
```

The application will be available at `http://127.0.0.1:8001/`

## 📁 Project Structure

```
chaiheadq/
├── chaiheadq/                 # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── tweet/                    # Tweet application
│   ├── models.py             # Tweet model definition
│   ├── views.py              # View logic
│   ├── forms.py              # Form definitions
│   ├── urls.py               # App URL patterns
│   └── templates/            # HTML templates
├── templates/                # Global templates
│   ├── layout.html           # Base template
│   └── registration/         # Auth templates
├── static/                   # Static files
│   └── css/
│       └── custom.css        # Custom styles
├── media/                    # User uploaded files
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create from template)
└── README.md                 # This file
```

## 🎯 Usage

### For Users

1. **Register/Login**: Create an account or login with existing credentials
2. **Create Tweets**: Click "New Tweet" to create posts with text and optional images
3. **View Tweets**: Browse all tweets on the home page
4. **Manage Content**: Edit or delete your own tweets
5. **Toggle Theme**: Switch between light and dark modes

### For Administrators

1. **Admin Access**: Visit `/admin/` and login with superuser credentials
2. **Content Management**: Manage all tweets and users through the admin panel
3. **User Management**: Create, edit, or delete user accounts

## 🔧 Configuration

### Environment Variables

The following environment variables can be configured in your `.env` file:

- `SECRET_KEY`: Django secret key for security
- `DEBUG`: Set to `True` for development, `False` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hostnames
- `DATABASE_URL`: Database connection string

### Static and Media Files

- Static files are served from the `static/` directory
- Media files (uploads) are stored in the `media/` directory
- Configure `STATIC_ROOT` and `MEDIA_ROOT` in settings for production

## 🚀 Deployment

### Production Setup

1. Set `DEBUG=False` in your environment variables
2. Configure a production database (PostgreSQL recommended)
3. Set up a web server (Nginx + Gunicorn recommended)
4. Configure static file serving
5. Set up proper security headers and HTTPS

### Example Production Commands

```bash
# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn chaiheadq.wsgi:application
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django framework and community
- Bootstrap for the responsive UI components
- All contributors and users of this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/chaiheadq/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

---

**Made with ❤️ using Django**

## 📸 Screenshots

_Add your screenshots here by uploading in the repo or using image links._

## 🚀 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django (Python)
- **Database:** SQLite3
- **Version Control:** Git & GitHub

## 📁 How to Run Locally

```bash
git clone https://github.com/sahilrai100/Django-tweet-app.git
cd Django-tweet-app

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver



1. go to github repo then `Add file` → `Upload files`.
2. Upload `screenshot1.png`, `screenshot2.png`, etc.
3. Fir README me yeh daal:

```markdown
## 📸 Screenshots

![Home Page](screenshot1.png)
![Tweet Form](screenshot2.png)
