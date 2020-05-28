import praw
import pickle
import urllib.request
reddit = praw.Reddit('bot1')

# for submission in reddit.subreddit('gaming').hot(limit=15):

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
    with open('resources/tracks/til_posts.txt', 'r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
            

    if len(posts)>50:
        posts=posts[-10:]

    for submission in reddit.subreddit('todayilearned').hot(limit=3):
        
        if not submission.stickied:
            if submission.id in posts:
                continue

            else:
                titles.append(submission.title)
                links.append(submission.url)
                new_posts.append(submission.id)
                # print(submission.permalink)

    posts = posts + new_posts            
        
    with open('resources/tracks/til_posts.txt', 'w') as filehandler:
        for listitem in posts:
            filehandler.write('%s\n' % listitem)

    return titles, links

def get_meme():
    titles, links, posts, new_posts = [], [], [], []
    with open('resources/tracks/meme_posts.txt', 'r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
    
    if len(posts) > 50:
        posts = posts[-15:]

    meme_multireddit = [mult for mult in reddit.redditor("69sloth").multireddits() if mult.path == '/user/69sloth/m/memes_for_bot']
    
    for submission in meme_multireddit[0].hot(limit=12):
        if submission.id in posts:
            continue
        else:
            # urllib.request.urlretrieve(submission.url, "resources/dank_memes/{}.jpg".format(submission.id))
            titles.append(submission.title)
            links.append(submission.url)
            new_posts.append(submission.id)
            # print(submission.permalink)

    posts = posts + new_posts
    
    with open('resources/tracks/meme_posts.txt', 'w') as filehandler:
        for listitem in posts:
            filehandler.write('%s\n' % listitem)  
    
    return titles, links

def get_pifs():
    print('inside get pifs line 84')
    titles, links, posts, new_posts = [], [], [], []
    with open('resources/tracks/pifs.txt','r') as filehandler:
        for line in filehandler:
            currentPost = line[:-1]
            posts.append(currentPost)
        
    if len(posts) > 50:
        posts = posts[-20:]

    nsfw_multireddit = [mult for mult in reddit.redditor("69sloth").multireddits() if mult.path == '/user/69sloth/m/nsfw_for_bot']

    # for submission in reddit.subreddit('gaming').hot(limit=15):   and not submission.url.startswith(matcher)
    matcher = ('https://redgifs','https://gfycat','https://i.imgur.com','https://i.redd.it/')
    for submission in nsfw_multireddit[0].hot(limit=15):
        if submission.id in posts or not submission.url.startswith(matcher):
            continue
        else:
            titles.append(submission.title)
            links.append(submission.url)
            new_posts.append(submission.id)
            # print(submission.permalink)
        
    posts = posts + new_posts
    
    with open('resources/tracks/pifs.txt', 'w') as filehandler:
        for listitem in posts:
            filehandler.write('%s\n' % listitem)

    return links

# if __name__ == "__main__":

#     link = get_pifs()
#     print(link)