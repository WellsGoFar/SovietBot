import praw
reddit = praw.Reddit('bot1')
for submission in reddit.subreddit('todayilearned').hot(limit=2):
    print(submission.id)
    print(submission.title)
    print(submission.url)
    print(submission.permalink)
    redditor = submission.author
    print(redditor)
    print(str(redditor.link_karma))
    print("----------------------------------------------------------------------------------+\n")