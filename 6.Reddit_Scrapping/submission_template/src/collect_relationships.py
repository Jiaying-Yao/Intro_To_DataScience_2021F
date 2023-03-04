import json
import bs4
import requests
import os.path as osp
import argparse

def retrieve(cache_dir, name):
    dating = []

    cache_file = osp.join(cache_dir, name)
    if not osp.exists(cache_file):
        link = f"https://www.whosdatedwho.com/dating/{name}"
        r = requests.get(link)
        with open(cache_file, 'w') as cache:
            cache.write(r.text)
        cache.close()
        r = open(cache_file, 'r')
    else:
        r = open(cache_file, 'r')

    try:
        soup = bs4.BeautifulSoup(r, 'html.parser')
        date_div = soup.find(id='ff-dating-history-grid')
        people = date_div.findAll(class_='ff-grid-box')
        for person in people:
            name1 = person['id']
            name1 = name1.split('-')
            name1 = "-".join(name1[1:])
            dating.append(name1)
    except Exception as err:
        print(f"information not available for {name}. Error:", err)
    r.close()
    
    return dating


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-c", "--config")
    parse.add_argument("-o", "--output")

    args = parse.parse_args()
    config_file = args.config
    output_file = args.output

    relations = dict()
    with open(config_file, 'r') as config:
        target = json.load(config)
        people = target["target_people"]
        cache_dir = target["cache_dir"]

        for person in people:
            relations[person] = retrieve(cache_dir, person)
    config.close()

    #save to output file
    with open(output_file, 'w') as output:
        output.truncate(0)
        json.dump(relations, output, indent=4, separators=(",", ":"))
    output.close()



if __name__ == '__main__':
    main()