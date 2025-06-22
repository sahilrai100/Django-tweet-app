import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaiheadq.settings')
django.setup()

from django.contrib.auth.models import User

# Get credentials from environment variables
username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@tweetbar.com')
password = os.getenv('ADMIN_PASSWORD', 'admin123')

try:
    # Check if superuser already exists
    if User.objects.filter(username=username).exists():
        print(f"✅ Superuser '{username}' already exists!")
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        # Create new superuser
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✅ Superuser created successfully!")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"User ID: {user.id}")
    
    print("\n🔗 Admin Panel URL: http://127.0.0.1:8001/admin/")
    
except Exception as e:
    print(f"❌ Error creating superuser: {e}") 