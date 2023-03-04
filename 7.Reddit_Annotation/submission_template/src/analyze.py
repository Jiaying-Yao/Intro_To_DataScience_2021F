'''
3.
run python3 analyze -i anno.tsv [-o output.json]
Output json counting for four post categories: "course-related", "food-related", "residence-related", "other" in tsv
'''
import argparse
import json
from os import sep
import pandas as pd
import os
import os.path

def main():
    #read commendline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--anno_tsv")
    parser.add_argument("-o", "--output", nargs='?')
    args = parser.parse_args()
    input_tsv = args.anno_tsv
    output = args.output

    #counts for 4 categories
    df = pd.read_csv(input_tsv, sep='\t')
    course,_ = df[df['coding']=='c'].shape
    food,_ = df[df['coding']=='f'].shape
    residence,_ = df[df['coding']=='r'].shape
    other,_ = df[df['coding']=='o'].shape

    json_out = {"course-related":course, "food-related":food, "residence-related":residence, "other":other}

    #output to stdout or outout file
    if output is None:
        print(json.dumps(json_out, indent=4))
    else:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, 'w') as f:
            f.truncate(0)
            json.dump(json_out, f, indent=4)
        f.close()

if __name__ == "__main__":
    main()