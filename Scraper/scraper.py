import requests
from datetime import datetime
import time
import json

start_time = datetime.utcnow()
url = "https://api.pushshift.io/reddit/{}/search?limit=1000&sort=desc&{}&before="

def redditScraper(subreddit):
    # subreddit = subredditName #subreddit you want to download
    filter_string = f"subreddit={subreddit}"
    print(f"Saving submissons to {subreddit}.json")

    count = 0
    previous_epoch = int(start_time.timestamp())
    file = open(f'{subreddit}.json', 'w', encoding='utf-8')
    while True:
        array = []
        new_url = url.format('submission', filter_string)+str(previous_epoch)
        req = requests.get(new_url,headers={'User-Agent': "Post downloader by /u/salman0ansari"})
        # print(new_url)
        time.sleep(1)
        try:
            res = req.json()
        except json.decoder.JSONDecodeError:
            time.sleep(1)
            continue
        SubData = res['data']
        if len(SubData) == 0:
                break
        for object in SubData:
            previous_epoch = object['created_utc'] - 1
            count += 1
            if object['is_self']:
                data = {}
                data['title'] = object['title']
                data['text'] = object['selftext']
                # data['flair'] = object['link_flair_text']

                array.append(data)
        
        json.dump(array, file, ensure_ascii=False, indent=4)
                
        print("Saved {} {} through {}".format(count, 'submissions', datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))
    print(f"Saved {count} {subreddit}s")
    file.close()


redditScraper("copypasta")