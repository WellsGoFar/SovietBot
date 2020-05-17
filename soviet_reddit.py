import praw
import pickle
import urllib.request
reddit = praw.Reddit('bot1')

# for submission in reddit.subreddit('dankmemes').hot(limit=15):

#     if (not submission.stickied):
#         print(submission.id)
#         print(submission.title)
#         print(submission.url)
#         print(submission.permalink)
#         redditor = submission.author
#         print(redditor)
#         print(str(redditor.link_karma))
#         print("\n\n")

def get_til():
    titles = []
    links = []
    posts = []
    new_posts = []
    pinned_post_counter = 0
    with open('tracks/til_posts.txt', 'r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
            

    if len(posts)>50:
        posts=posts[24:]

    for submission in reddit.subreddit('todayilearned').hot(limit=5):
        
        if not submission.stickied:
            if submission.id in posts:
                continue

            else:
                titles.append(submission.title)
                links.append(submission.url)
                new_posts.append(submission.id)

    posts = posts + new_posts            
        
    with open('tracks/til_posts.txt', 'w') as filehandler:
        for listitem in posts:
            filehandler.write('%s\n' % listitem)

    return titles, links

def get_meme():
    titles, links, posts, new_posts = [], [], [], []
    with open('tracks/meme_posts.txt', 'r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
    
    if len(posts) > 100:
        posts = posts[49:]

    meme_multireddit = [mult for mult in reddit.redditor("69sloth").multireddits() if mult.path == '/user/69sloth/m/memes_for_bot']
    
    for submission in meme_multireddit[0].hot(limit=12):
        if submission.id in posts:
            continue
        else:
            urllib.request.urlretrieve(submission.url, "dank_memes/{}.jpg".format(submission.id))
            titles.append(submission.title)
            links.append(submission.url)
            new_posts.append(submission.id)
            # print(submission.permalink)

    posts = posts + new_posts
    
    with open('tracks/meme_posts.txt', 'w') as filehandler:
        for listitem in posts:
            filehandler.write('%s\n' % listitem)  
    
    return titles, links

def get_pifs():
    titles, links, posts, new_posts = [], [], [], []
    with open('tracks/pifs.txt','r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
        
    if len(posts) > 200:
        posts = posts[99:]

    nsfw_multireddit = [mult for mult in reddit.redditor("69sloth").multireddits() if mult.path == '/user/69sloth/m/nsfw_for_bot']

    for submission in nsfw_multireddit[0].hot(limit=15):

        if submission.id in posts:
            continue
        else:
            titles.append(submission.title)
            links.append(submission.url)
            new_posts.append(submission.id)
        
    posts = posts + new_posts
    
    with open('tracks/pifs.txt', 'w') as filehandler:
        for listitem in posts:
            filehandler.write('%s\n' % listitem)

    return links

# if __name__ == "__main__":

    # get_pifs()
    # print(links)