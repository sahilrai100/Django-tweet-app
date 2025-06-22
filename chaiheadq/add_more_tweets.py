import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaiheadq.settings')
django.setup()

from django.contrib.auth.models import User
from tweet.models import Tweet

# Get or create users
users = []
for username in ['anime_lover', 'cartoon_fan', 'pokemon_trainer']:
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'email': f'{username}@example.com'}
    )
    if created:
        user.set_password('password123')
        user.save()
    users.append(user)

# Create tweets with different images
tweets_data = [
    {
        'user': users[0],
        'text': 'Doraemon is such a classic! 🐱 The gadgets are so creative and the friendship between Nobita and Doraemon is heartwarming. #Doraemon #ClassicAnime',
        'photo': 'photos/doramon_img.jpg'
    },
    {
        'user': users[1],
        'text': 'Ninja Hattori is amazing! 🥷 The ninja techniques and the bond between Hattori and Kenichi is so cool. #NinjaHattori #Ninja',
        'photo': 'photos/ninja_hatori.jpg'
    },
    {
        'user': users[2],
        'text': 'Pikachu is the cutest Pokemon! ⚡ Pikachu and Ash\'s friendship is legendary. #Pokemon #Pikachu #Ash',
        'photo': 'photos/char-pikachu.png'
    }
]

for tweet_data in tweets_data:
    Tweet.objects.create(**tweet_data)

print("✅ Added more tweets with images!")
print("🖼️  All images should now load properly!") 