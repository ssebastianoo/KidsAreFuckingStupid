import telepot, requests, json, time, os, dotenv

dotenv.load_dotenv(dotenv_path = ".env")

def bitly(url):
    headers = {
    'Authorization': f'Bearer {os.environ["bitly"]}',
    'Content-Type': 'application/json',
    }

    data = '{"long_url": "' + url + '", "domain": "bit.ly"}'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
    res = response.json()

    return res["link"]

bot = telepot.Bot(os.environ["token"])
print("ready")

while True:
    url = "https://www.reddit.com/r/KidsAreFuckingStupid/hot.json"
    res = requests.get(url, headers = {'User-agent': 'sebamemes by u/sebastianogirotto'})
    res = res.json()
    url = res["data"]["children"][0]["data"]["url_overridden_by_dest"]
    author = "u/" + res["data"]["children"][0]["data"]["author"]
    subreddit = "r/" + res["data"]["children"][0]["data"]["subreddit"]
    ups = res["data"]["children"][0]["data"]["ups"]
    title = res["data"]["children"][0]["data"]["title"]
    link = "https://reddit.com" + res["data"]["children"][0]["data"]["permalink"]
    link = bitly(link)

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

        caption = f"• *{title}*\n\n• by *{author}*\n\n• *{ups}* upvotes\n\n• {link}"

        if url.endswith(("png", "jpg", "jpeg")):
            bot.sendPhoto(-1001410145919, url, caption = caption, parse_mode = "Markdown")
        
        elif ".mp4" in url or ".gif" in url:
            bot.sendVideo(-1001410145919, url, caption = caption, parse_mode = "Markdown")

    time.sleep(120) 