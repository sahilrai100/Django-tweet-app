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

def cleanup_and_create_tweets():
    print("🔄 Cleaning up old tweets and creating new ones...")
    
    # Delete tweets older than 2 days
    cutoff_date = datetime.now() - timedelta(days=2)
    old_tweets = Tweet.objects.filter(created_at__lt=cutoff_date)
    deleted_count = old_tweets.count()
    old_tweets.delete()
    print(f"🗑️  Deleted {deleted_count} old tweets")
    
    # Get or create a test user
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
    )
    
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"👤 Created test user: {user.username}")
    else:
        print(f"👤 Using existing user: {user.username}")
    
    # Delete existing dummy tweets
    Tweet.objects.filter(user=user).delete()
    
    # Create 3 new dummy tweets
    dummy_tweets = [
        {
            'text': 'Just had the most amazing coffee! ☕ The aroma is absolutely divine. Perfect way to start the day! #CoffeeLover #MorningVibes',
            'user': user
        },
        {
            'text': 'Working on some exciting new features for our project! 💻 The code is coming together beautifully. Can\'t wait to share the results! #Coding #Development',
            'user': user
        },
        {
            'text': 'Beautiful sunset today! 🌅 Nature never fails to amaze me. Sometimes you just need to pause and appreciate the little moments in life. #Sunset #Nature',
            'user': user
        }
    ]
    
    created_tweets = []
    for tweet_data in dummy_tweets:
        tweet = Tweet.objects.create(**tweet_data)
        created_tweets.append(tweet)
        print(f"📝 Created tweet: {tweet.text[:50]}...")
    
    print(f"✅ Successfully created {len(created_tweets)} new tweets!")
    print("🚀 Ready to run the server!")

if __name__ == '__main__':
    cleanup_and_create_tweets() 