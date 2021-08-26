# @commands.command()
async def gif (self, ctx, *, search_term='trending_right_now_19190572'):

    try:
        if "ashwin" in search_term:
            await ctx.send("**fuck off retard**")
        else:
            apikey = "8LKJCTB3AWSH"  
            lmt = 10
            search_term = search_term
            # async with ctx.typing():
            await ctx.trigger_typing()
            if search_term == 'trending_right_now_19190572':
                r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (apikey, lmt))
            else:
                r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

            if r.status_code == 200:
                top_gifs = json.loads(r.content)
            else:
                top_gifs = None

            if top_gifs is not None and len(top_gifs['results']) != 0:
                n = random.randint(0,len(top_gifs['results']))
                gif_msg = await ctx.send(top_gifs['results'][n]['url'])
                msg_id = gif_msg.id

                # await gif_msg.add_reaction('✅')
                # await gif_msg.add_reaction('❎')
                
            
            else:
                await ctx.send('**cyka blyat, that returned no results**')

    except Exception as e:
        await ctx.send('**cyka blyat, that returned no results**')
        print(e)

st = "hi {} there".format('|'*3)
print(st)
