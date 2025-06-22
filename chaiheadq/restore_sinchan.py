#!/usr/bin/env python
import os
import sys
import django
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaiheadq.settings')
django.setup()

from django.contrib.auth.models import User
from tweet.models import Tweet

def restore_sinchan_and_fix_images():
    print("🔄 Restoring Sinchan data and fixing images...")
    
    # Get or create users
    users_data = [
        {
            'username': 'sinchan_fan',
            'email': 'sinchan@example.com',
            'first_name': 'Sinchan',
            'last_name': 'Fan'
        },
        {
            'username': 'anime_lover',
            'email': 'anime@example.com',
            'first_name': 'Anime',
            'last_name': 'Lover'
        },
        {
            'username': 'cartoon_world',
            'email': 'cartoon@example.com',
            'first_name': 'Cartoon',
            'last_name': 'World'
        }
    ]
    
    created_users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults=user_data
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"👤 Created user: {user.username}")
        created_users.append(user)
    
    # Create tweets with images
    tweets_data = [
        {
            'user': created_users[0],
            'text': 'Crayon Shin-chan is the best anime ever! 🎨 Shin-chan always makes me laugh with his funny antics. #CrayonShinChan #Anime #Funny',
            'photo': 'photos/shirow_image.jpg'
        },
        {
            'user': created_users[1],
            'text': 'Doraemon is such a classic! 🐱 The gadgets are so creative and the friendship between Nobita and Doraemon is heartwarming. #Doraemon #ClassicAnime',
            'photo': 'photos/doramon_img.jpg'
        },
        {
            'user': created_users[2],
            'text': 'Ninja Hattori is amazing! 🥷 The ninja techniques and the bond between Hattori and Kenichi is so cool. #NinjaHattori #Ninja',
            'photo': 'photos/ninja_hatori.jpg'
        },
        {
            'user': created_users[0],
            'text': 'Chhota Bheem is our Indian superhero! 💪 The stories are so engaging and teach great values. #ChhotaBheem #IndianCartoon',
            'photo': 'photos/bheem_img.jpg'
        },
        {
            'user': created_users[1],
            'text': 'Pikachu is the cutest Pokemon! ⚡ Pikachu and Ash\'s friendship is legendary. #Pokemon #Pikachu #Ash',
            'photo': 'photos/char-pikachu.png'
        }
    ]
    
    # Delete existing tweets from these users
    for user in created_users:
        Tweet.objects.filter(user=user).delete()
    
    # Create new tweets
    created_tweets = []
    for tweet_data in tweets_data:
        # Set created_at to be 3 days ago for the first tweet (Sinchan)
        if 'Crayon Shin-chan' in tweet_data['text']:
            tweet_data['created_at'] = datetime.now() - timedelta(days=3, hours=19)
        
        tweet = Tweet.objects.create(
            user=tweet_data['user'],
            text=tweet_data['text'],
            photo=tweet_data['photo']
        )
        
        if 'created_at' in tweet_data:
            tweet.created_at = tweet_data['created_at']
            tweet.save()
        
        created_tweets.append(tweet)
        print(f"📝 Created tweet with image: {tweet.text[:50]}...")
    
    print(f"✅ Successfully created {len(created_tweets)} tweets with images!")
    print("🖼️  Images should now load properly!")
    print("🚀 Ready to run the server!")

if __name__ == '__main__':
    restore_sinchan_and_fix_images() 