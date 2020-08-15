import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tesdb"]
mycol = mydb["testcollection"]

# mydoc = mycol.find()

# data = {'guildID': 547139967529517059, 'nsfw_channel': 711352385292992545, 'meme_channel': 694190991657402498, 'facts_chanel': 710121490212978809}

# y = mycol.insert_one(data)


mydoc = mycol.find()
for x in mydoc:
    print(x['guildID'])
    print(x['facts_channel'])
