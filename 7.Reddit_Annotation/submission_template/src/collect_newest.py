'''
1.
run python3 collect_newest.py -o subreddit_name.json -s /r/subreddit_name
write 100 newest posts into subreddit_name.jso line by line
'''
import requests
import requests.auth
import argparse
import os
import os.path as osp
import json

#authentication information
auth = requests.auth.HTTPBasicAuth('ILWibcPhrsvU3Qbz0Uz__g','D1sFSUUYYpW-hDuv6Jkb1Hi0-0U9XA')
post_data = {"grant_type": "password", "username": "Jenny_huff", "password": "123456jenny"}
headers = {"User-Agent": "ChangeMeClient/0.1 by Jenny_huff"}

#return a json fetched from reddit/r/subred
def retrieve(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    cache_file = osp.join("..","data",f"{subreddit}.cache.json")
    os.makedirs(os.path.dirname(cache_file), exist_ok=True)

    #chech cache
    if not osp.exists(cache_file):
        print(f"Fetching {subreddit} from reddit")
        r = requests.get(url, auth=auth, data=post_data, headers=headers, params={'limit' : 100})
        root_element = r.json()

        with open(cache_file, "w") as f:
            json.dump(root_element, f)
        f.close()

    else:
        print(f"Loading from cache file: {cache_file}")
        with open(cache_file, "r") as f:
            root_element = json.load(f)
        f.close()

    return root_element['data']['children']

def main():
    #read from command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    parser.add_argument("-s", "--subreddit")
    args = parser.parse_args()
    output = args.output
    subreddit = args.subreddit.split("/")[2]
    print(subreddit)

    elements = retrieve(subreddit)
    line_count = 0

    #create the directory if not exist
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, 'w') as out:
        out.truncate(0)
        for element in elements:
            json.dump(element, out)
            if line_count < 99:
                out.write("\n")
            line_count = line_count + 1
    out.close()


if __name__ == '__main__':
    main()