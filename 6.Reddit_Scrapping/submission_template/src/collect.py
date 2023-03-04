import requests
import requests.auth
import sys, os
import os.path as osp
import json


#authentication information
auth = requests.auth.HTTPBasicAuth('ILWibcPhrsvU3Qbz0Uz__g','D1sFSUUYYpW-hDuv6Jkb1Hi0-0U9XA')
post_data = {"grant_type": "password", "username": "Jenny_huff", "password": "123456jenny"}
headers = {"User-Agent": "ChangeMeClient/0.1 by Jenny_huff"}

#output files
dir_path = osp.dirname(__file__)
SAMPLE_FILE1 = osp.join(dir_path, "..", "sample1.json")
SAMPLE_FILE2 = osp.join(dir_path, "..", "sample2.json")

#subreddit names
red_sample1 = ['funny', 'AskReddit', 'gaming', 'aww', 'pics', 'Music', 'science', 'worldnews', 'videos', 'todayilearned']
red_sample2 = ['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends', 'unpopularopinion']

def retrieve(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    CACHE_FILE = f"../data/{subreddit}.cache.json"

    #check cache
    if not osp.exists(CACHE_FILE):
        print(f"Fetching {subreddit}")
        r = requests.get(url, auth=auth, data=post_data, headers=headers, params={'limit' : 100})
        root_element = r.json()

        with open(CACHE_FILE, 'w') as f:
            json.dump(root_element, f)
        f.close()
    else:
        print(f"Loading {subreddit} from cache")
        with open(CACHE_FILE, "r") as f:
            root_element = json.load(f)
        f.close()

    return root_element['data']['children']


def main():
    line_count1 = 0
    if not osp.exists(SAMPLE_FILE1):
        with open(SAMPLE_FILE1, 'w') as sf1:
            sf1.truncate(0)
            for red in red_sample1:
                elements = retrieve(red)
                for element in elements:
                    json.dump(element, sf1)
                    if line_count1 < 999:
                        sf1.write("\n")
                    line_count1 = line_count1 + 1
        sf1.close()
    print("Sample1 stored in file sample1.json, delete if you want to update contents")

    line_count2 = 0
    if not osp.exists(SAMPLE_FILE2):
        with open(SAMPLE_FILE2, 'w') as sf2:
            sf2.truncate(0)
            for red in red_sample2:
                elements = retrieve(red)
                for element in elements:
                    json.dump(element, sf2)
                    if line_count2 < 999:
                        sf2.write("\n")
                    line_count2 = line_count2 + 1
        sf2.close()
    print("Sample2 stored in file sample2.json, delete if you want to update contents")


if __name__ == '__main__':
    main()
