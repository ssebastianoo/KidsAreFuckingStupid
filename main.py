import telepot, requests, json, time, os, dotenv, traceback

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
chatid = int(os.environ["id"])
print("ready")

while True:
    try:
        url = "https://www.reddit.com/r/KidsAreFuckingStupid/hot.json"
        res = requests.get(url, headers = {'User-agent': 'sebamemes by u/sebastianogirotto'})
        res = res.json()

        for post in range(10):
            url = res["data"]["children"][post]["data"]["url_overridden_by_dest"]
            author = "u/" + res["data"]["children"][post]["data"]["author"]
            subreddit = "r/" + res["data"]["children"][post]["data"]["subreddit"]
            ups = res["data"]["children"][post]["data"]["ups"]
            title = res["data"]["children"][post]["data"]["title"]
            link = "https://reddit.com" + res["data"]["children"][post]["data"]["permalink"]
            link = bitly(link)

            if "v.redd.it" in url:
                url = res["data"]["children"][post]["data"]["media"]["reddit_video"]["fallback_url"]

            f = open("url.txt", "r")
            f_ = f.read()

            posted = f_.split("\n")

            print(url)

            if url in posted:
                f.close()
                print("already posted")
                pass

            else:
                if len(posted) >= 50:
                    posted.pop(0)

                posted.append(url)

                # remove all the blank fields

                passed = False 

                while not passed:
                    if " " in posted:
                        posted.remove(" ")
                        passed = False

                    else:
                        passed = True

                f = open("url.txt", "w")
                f.write("\n".join(posted))
                f.close()

                caption = f"• *{title}*\n\n• by *{author}*\n\n• *{ups}* upvotes\n\n• {link}"

                if url.endswith(("png", "jpg", "jpeg")):
                    bot.sendPhoto(chatid, url, caption = caption, parse_mode = "Markdown")
                
                elif ".mp4" in url or ".gif" in url:
                    bot.sendVideo(chatid, url, caption = caption, parse_mode = "Markdown")

    except Exception as e:
        bot.sendMessage(int(os.environ["logs_id"]), str(e))

    time.sleep(120) 