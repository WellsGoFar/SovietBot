# SovietBot

This is the code for SovietBot, a bot that crossposts content from Reddit to your Discord Server.

## Running it:

Note: This requires you to have python3 installed.

You will also need to setup a mongoDB cluster running.

```
git clone https://github.com/WellsGoFar/SovietBot.git
./scripts/setup.sh
```

Once the dependencies are installed and the files are cloned, you can setup your MongoDB cluster and change the `MongoClient` address to your clusters address (leave it same if you are running a standalone cluster on your local machine). You will also need to change the database name and collection name in the following files:

* server_config.py
* imdad.py
* reddithandler.py 
* greetings.py

After all that is out of the way, you can run the bot with:

```
python SovietBot/src/bot.py
```

## Adding the SovietBot to your Discord server:

To add the SovietBot to your server, simply click [here](https://discord.com/api/oauth2/authorize?client_id=710663310965473302&permissions=1275554928&scope=bot).

Once the bot is added, it will ask you set the channels where you want memes, fun facts, server logs etc.

You will see a message like this:

![first setup message](./img/intro.png)

After you run the command you'll get instructions to setup channels for different content:

![adding channels](./img/channel.png)

Once the setup process is complete you get this message:

![adding channels](./img/done.png)

## Contact

Don't hesitate to contact me [here](https://www.linkedin.com/in/ashwin-bhatnagar/) if you have any questions regarding the setup process.

Cheers!