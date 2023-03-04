'''
2.
run python3 extract_to_tsv.py -o output.tsv subreddit.json n(num of lines)
write to output.tsv, id and title for n random posts in subreddit
'''
import pandas as pd
import os
import os.path as osp
import argparse
import random
import json

def main():
    #read command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    parser.add_argument("json_file")
    parser.add_argument("nums_post")

    args = parser.parse_args()

    output = args.output
    json_file = args.json_file
    nums = int(args.nums_post)

    output_df = pd.DataFrame(data={'Name':[],'title':[],'coding':[]})

    with open(json_file, 'r') as js:
        lines = js.readlines()
        total_post = len(lines)

        #if want to generate more lines
        if nums >= total_post:
            for line in lines:
                post = json.loads(line)
                name = post['data']['author_fullname']
                title = post['data']['title']
                df_append = pd.DataFrame({'Name':[name], 'title':[title]})
                output_df = output_df.append(df_append, ignore_index=True)
        else:
            #shuffle all lines than select the first n
            random.shuffle(lines)
            for i in range(nums):
                post = json.loads(lines[i])
                name = post['data']['author_fullname']
                title = post['data']['title']
                df_append = pd.DataFrame({'Name':[name], 'title':[title]})
                output_df = output_df.append(df_append, ignore_index=True)
            
    js.close()

    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, 'w') as output:
        output.truncate(0)
        output_df.to_csv(output, index=False, encoding='utf-8', sep='\t')
    output.close()



if __name__ == '__main__':
    main()