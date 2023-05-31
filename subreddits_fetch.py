import praw
import csv

# Reddit API credentials
client_id='GffiDK_HkVYNW84hPOIfQw'
client_secret='Mf2UYpwX4R6cweW0yaK65UrLCAh3YQ'
username='Leather-Extent1679'
password='Fran@98118'
user_agent='MLResearch/1.0'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent
                     )

csv_file = 'subreddits.csv'
fieldnames = ['Subreddit','Subscribers','Description']

all_subreddits = reddit.subreddits.popular(limit=None)  # Fetches all subreddits

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for subreddit in all_subreddits:
        writer.writerow({'Subreddit': subreddit.display_name,
                         'Subscribers': subreddit.subscribers,
                         'Description': subreddit.public_description})
