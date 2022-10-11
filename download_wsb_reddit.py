import csv
from datetime import datetime
import os

from praw import Reddit
from psaw import PushshiftAPI


def get_date(created):
    return datetime.fromtimestamp(created)


def reddit_connection() -> Reddit: #get reddit connection 
    personal_use_script = "xxxxxxxxxxxxxxxxxx" #enter your own personal_use_script from 'create application' https://www.reddit.com/prefs/apps/
    client_secret = "xxxxxxxxxxxxxxxxxxx" #enter your own secret key from 'create application' https://www.reddit.com/prefs/apps/
    user_agent = "testscript by yanying"

    reddit = Reddit(client_id=personal_use_script,
                    client_secret=client_secret,
                    user_agent=user_agent)
    return reddit


def download(): 
    search = pushshift.search_submissions(subreddit='WallStreetBets', 
                                          size=500,
                                          user_removed=False,
                                          mod_removed=False)  #return a submission iterator 

    i = 0
    for s in search:
        print(f"{i}: Processing submission {s.id} {get_date(s.created)}")
        process_submission(s.id) #download the submission and comments 
        file.flush()
        i += 1


def process_submission(id):
    data = reddit.submission(id=id)._fetch_data() #use reddit api to download the raw data 
    list = [child for d in data for child in d['data']['children']]
    submission = [child['data'] for child in list if child['kind'] == 't3'][0] #get submission data - one submission
    comments = [child['data'] for child in list if child['kind'] == 't1'] #get comments data - a list of comments 

    if not process_submission_data(submission):
        # print("Submission is removed")
        return

    for comment in comments:
        process_comment_data(comment)


def process_submission_data(submission):
    """
    Returns True if the submission is not removed, False otherwise.
    """
    # print(f"Processing submission {submission['title']}")
    if submission['removed_by_category'] is not None: #if the submission is removed by reddit then don't do anything 
        return False

    writer.writerow([
        submission['id'],
        submission['title'],
        submission['url'],
        submission['score'],
        submission['num_comments'],
        submission['selftext'],
        get_date(submission['created_utc']),
    ])
    return True


def process_comment_data(comment):
    # print(f"Processing comment {comment['body']}")
    writer.writerow([
        comment['id'],
        "Comment",
        comment['link_id'].split('_')[1], 
        comment['score'],
        0,
        comment['body'],
        get_date(comment['created_utc']),
    ])


if __name__ == "__main__":
    reddit = reddit_connection() #get reddit connection so to get each submission and comment 
    pushshift = PushshiftAPI(reddit) #use pushshift api for historical submission IDs because reddit api doesn't support historical search (you need to get a list of ID)
    file = open('wsb.csv', 'w') #output file 
    writer = csv.writer(file, lineterminator='\n') #csv writer 
    writer.writerow(['id', 'title', 'url', 'score',
                    'num_comments', 'body', 'created']) #header 
    download()
