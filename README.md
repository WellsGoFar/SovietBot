# SovietBot

This is the code for SovietBot, a bot that crossposts content from Reddit to your Discord Server and has amazing features like gifs and server moderation.

## Running it:

Note: This requires you to have python3 installed.

You will also need to setup a mongoDB cluster running.

```
git clone https://github.com/WellsGoFar/SovietBot.git
```

You will also need to install the following libraries:

```
pip install discord.py
pip install praw
pip install asyncio
pip install python-dotenv
pip install pymongo
```

Once the dependencies are installed and the files are cloned, you can setup your MongoDB cluster and change the `MongoClient` address to your clusters address (leave it same if you are running a standalone cluster on your local machine). You will also need to change the database name and collection name in the following files:

* src/cogs/server_config.py
* src/cogs/imdad.py
* src/cogs/reddithandler.py 
* src/cogs/greetings.py

After all that is out of the way, you can run the bot with:

```
python SovietBot/src/bot.py
```

## Adding the SovietBot to your Discord server:

To add the SovietBot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=710663310965473302&permissions=1275554928&scope=bot).

Once the bot is added, it will ask you set the channels where you want memes, fun facts, server logs etc.

You will see a message like this:

![first setup message](https://github.com/WellsGoFar/SovietBot/blob/master/img/intro.PNG?raw-true)

After you run the command you'll get instructions to setup channels for different content:

![adding channels](https://github.com/WellsGoFar/SovietBot/blob/master/img/channel.PNG?raw-true)

Once the setup process is complete you get this message:

![complete setup](https://github.com/WellsGoFar/SovietBot/blob/master/img/done.PNG?raw-true)

## Contact

Don't hesitate to contact me [here](https://www.linkedin.com/in/ashwin-bhatnagar/) if you have any questions regarding the setup process or want to suggect new features for the SovietBot.

Cheers!
