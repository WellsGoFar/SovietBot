import praw
import pickle
reddit = praw.Reddit('bot1')

# for submission in reddit.subreddit('todayilearned').hot(limit=3):

#     print(submission.id)
#     print(submission.title)
#     print(submission.url)
#     print(submission.permalink)
#     redditor = submission.author
#     print(redditor)
#     print(str(redditor.link_karma))
#     print("\n\n")

def get_til():
    titles = []
    links = []
    posts = []
    new_posts = []
    with open('tracks/til_posts.txt', 'r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
            

    if len(posts)>50:
        posts=posts[24:]

    for submission in reddit.subreddit('todayilearned').hot(limit=5):
        
        if submission.id in posts:
            continue

        else:
            titles.append(submission.title)
            links.append(submission.url)
            new_posts.append(submission.id)

    with open('tracks/til_posts.txt', 'a') as filehandler:
        for listitem in new_posts:
            filehandler.write('%s\n' % listitem)
    
    return titles, links
    
if __name__ == "__main__":
    titles, links = get_til()
    print(len(titles), len(links))