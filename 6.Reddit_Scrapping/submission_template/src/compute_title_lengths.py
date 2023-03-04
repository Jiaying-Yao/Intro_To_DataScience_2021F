import sys, os
import os.path as osp
import json
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()
    input_file = args.input
    length = []

    with open(input_file, "r", encoding='utf-8') as f:
        for line in f:
            post = json.loads(line)
            try:
                title = post['data']['title']
                length.append(len(title))
            except KeyError as err:
                length.append(0)

        f.close()
    print(sum(length)/len(length))

if __name__ == "__main__":
    main()

