# django
# Django Tweet App 🐦

A simple tweet posting web app built using **Django** framework.  
Users can create, edit, delete tweets, and upload photos with them.

## 🔧 Features

- ✅ User Authentication (Login/Logout/Register)
- ✅ Create Tweet (with text + optional photo)
- ✅ Edit / Delete Tweet
- ✅ View All Tweets
- ✅ Django Admin Panel

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



