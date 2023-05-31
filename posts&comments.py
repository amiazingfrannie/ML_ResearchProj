import praw
import pandas as pd
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
subreddit = reddit.subreddit("mentalhealth")

# Scraping the top posts of all time
posts = subreddit.top(time_filter = "all", limit = None)
 
posts_dict = {"Title": [], "Post Text": [], "Author": [], "ID": [], "Score": [],
              "Total Comments": [],"Created On":[], "Post URL": [],
              "Original Content": [], "Edited": [], "Saved": []
              }

comments_dict = {
    "Author": [],
    "Comment": [],
    "Created On": [],
    "Post ID": []
}

start_date = datetime.datetime(2023, 1, 1)

for post in posts:
    # Date of each post's creation
    date = datetime.datetime.fromtimestamp(post.created_utc)
    if date > start_date:
        # Title of each post
        posts_dict["Title"].append(post.title)

        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)

        # Author of the post
        posts_dict["Author"].append(post.author.name if post.author else "[deleted]")

        # Unique ID of each post
        posts_dict["ID"].append(post.id)

        # The score of a post
        posts_dict["Score"].append(post.score)

        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)

        # Date the post was created
        posts_dict["Created On"].append(date)

        # URL of each post
        posts_dict["Post URL"].append(post.url)

        # Flair of each post
        posts_dict["Original Content"].append(post.is_original_content)

        # Edited Check for each post
        posts_dict["Edited"].append(post.edited)

        # Saved check for each post
        posts_dict["Saved"].append(post.saved)

        # Access the comments of the post
        post.comments.replace_more(limit=None)
        comments = post.comments.list()

        # Iterate over the comments and append to the comments_dict
        for comment in comments:
            comments_dict["Author"].append(comment.author.name if comment.author else "[deleted]")
            comments_dict["Comment"].append(comment.body)
            comments_dict["Created On"].append(datetime.datetime.fromtimestamp(comment.created_utc))
            comments_dict["Post ID"].append(post.id)

# Saving the data in pandas dataframes
all_posts = pd.DataFrame(posts_dict)
all_comments = pd.DataFrame(comments_dict)

all_posts.to_csv("posts_data.csv", index=False)
all_comments.to_csv("comments_data.csv", index=False)