import telepot, requests, json, time

bot = telepot.Bot("1123360447:AAHCkIcgJnPg7eb5WOxOk3uSvdPuLaXm2w8")
print("ready")

while True:
    url = "https://www.reddit.com/r/KidsAreFuckingStupid/new.json"
    res = requests.get(url, headers = {'User-agent': 'sebamemes by u/sebastianogirotto'})
    res = res.json()
    url = res["data"]["children"][0]["data"]["url_overridden_by_dest"]
    author = "u/" + res["data"]["children"][0]["data"]["author"]
    subreddit = "r/" + res["data"]["children"][0]["data"]["subreddit"]
    ups = res["data"]["children"][0]["data"]["ups"]
    title = res["data"]["children"][0]["data"]["title"]

    if "v.redd.it" in url:
        url = res["data"]["children"][0]["data"]["media"]["reddit_video"]["fallback_url"]

    f = open("url.txt", "r")
    f_ = f.read()

    print(url)

    if str(f_) == url:
        f.close()
        print("same url, passed")
        pass

    else:
        f = open("url.txt", "w")
        f.write(url)
        f.close()

        caption = f"• *{title}*\n\n• by *{author}*\n\n• *{ups}* upvotes"

        # parse_mode = "Markdown"

        if url.endswith(("png", "jpg", "jpeg")):
            bot.sendPhoto(-1001410145919, url, caption = caption, parse_mode = "Markdown")

        elif ".gif" in url:
            bot.sendAnimation(-1001410145919, url, caption = caption, parse_mode = "Markdown")
        
        elif ".mp4" in url:
            bot.sendVideo(-1001410145919, url, caption = caption, parse_mode = "Markdown")

    time.sleep(120)