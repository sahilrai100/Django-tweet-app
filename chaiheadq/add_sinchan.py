import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaiheadq.settings')
django.setup()

from django.contrib.auth.models import User
from tweet.models import Tweet

# Create Sinchan user
user, created = User.objects.get_or_create(
    username='sinchan_fan',
    defaults={'email': 'sinchan@example.com'}
)
if created:
    user.set_password('password123')
    user.save()

# Create Sinchan tweet with image
tweet = Tweet.objects.create(
    user=user,
    text='Crayon Shin-chan is the best anime ever! 🎨 Shin-chan always makes me laugh with his funny antics. #CrayonShinChan #Anime #Funny',
    photo='photos/shirow_image.jpg'
)

# Set the timestamp to 3 days 19 hours ago
tweet.created_at = datetime.now() - timedelta(days=3, hours=19)
tweet.save()

print("✅ Sinchan data restored!")
print("🖼️  Image should now load properly!") 