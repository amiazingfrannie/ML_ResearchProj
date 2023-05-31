
import praw
import csv
import datetime

# Reddit API credentials
client_id='GffiDK_HkVYNW84hPOIfQw'
client_secret='Mf2UYpwX4R6cweW0yaK65UrLCAh3YQ'
username='Leather-Extent1679'
password='Fran@98118'
user_agent='MLResearch/1.0'

# Initialize the Reddit API client
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent
                     )

# Subreddits to fetch comments from
subreddit_names = ['ChatGPT']  
start_timestamp = datetime.datetime(2023, 1, 1).timestamp()  
end_timestamp = datetime.datetime(2023, 2, 1).timestamp()  

def fetch_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    comments = []
    
    for comment in subreddit.comments.list():
        if start_timestamp <= comment.created_utc <= end_timestamp:
            print(comment)
            comments.append(comment)
    
    return comments

all_comments = []

for subreddit_name in subreddit_names:
    comments = fetch_comments(subreddit_name)
    all_comments.extend(comments)

csv_file = 'comments_data.csv'
fieldnames = ['Comment', 'Subreddit', 'Author', 'Timestamp']

with open(csv_file, 'a', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    if file.tell() == 0:
        writer.writeheader()

    for comment in all_comments:
        writer.writerow({'Comment': comment.body,
                         'Subreddit': comment.subreddit.display_name,
                         'Author': comment.author.name,
                         'Timestamp': datetime.datetime.fromtimestamp(comment.created_utc)})