import pandas as pd
#for input parsing
import sys, os
import os.path as osp
import argparse
import json
from jsonschema import validate
#for date parsing
import datetime
import pytz
import dateutil.parser as parser

schema = {
    "type" : "object",
    "properties" : {
        "title" : {"type" : "string"},
        "title_text" : {"type": "string"},
        "createdAt" : {
            "type" : "string", 
            "format" : "date-time"
        },
        "text" : {"type" : "string"},
        "author" : {"type" : "string"},
        "total_count" : {
            #8. must be int float or string
            "type" : ["number", "string"]
        },
        "tags" : {"type" : "array"}
    },
    #1. requires title ot title_text
    "anyOf" : [
        {"required" : ["title"]},
        {"required" : ["title_text"]}
    ]
}

#check if in correct json format
def check_json(line):
    try:
        temp = json.loads(line)
        validate(temp, schema) 
        return temp
    except Exception as err:
        return -1

#2. rename into title
def rename_title(js):
    try:
        js['title'] = js.pop('title_text')
        return js
    except KeyError as err:
        try:
            title = js['title']
            return js
        except KeyError as err:
            return -1

#3. Standardize createdAt date times to the UTC timezone
#4. remove if date time that can’t be parsed using the ISO datetime standard
#did not check if createdAt is of type date
def stand_date(js):
    try:
        date = js['createdAt']
    except KeyError as err1:
        return js
    
    try:
        date = parser.parse(date)
        js['createdAt'] = date.astimezone(pytz.utc).isoformat()
        return js
    except Exception as err2:
        return -1

#6. Remove all the posts where the author field is empty, null, or N/A.
def check_author(js):
    try:
        author = js['author']
        if author == 'null' or author == 'N/A' or len(author)==0 or author == None:
            return -1
        else:
            return js
    except KeyError as err:
        return js

#7.  total_count: change float and string to int
def check_count(js):
    try:
        count = js['total_count']
    except KeyError as err:
        return js
    
    try:
        js['total_count'] = int(count)
        return js
    except ValueError as err2:
        return -1

#9. slice tags[] into individual words
def slice_tag(js):
    try:
        tags = js['tags']
        sentence = " ".join(tags)
        js['tags'] = sentence.split()
        return js
    
    except KeyError as err:
        return js


def main():
    #parse input and output files from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input')
    parser.add_argument('-o','--output')
    args = parser.parse_args()
    
    #script_dir = osp.dirname(__file__)
    #input = osp.join(script_dir, args.input)
    #output = osp.join(script_dir, args.output)
    print(args.input)

    input = args.input
    output = args.output
    #open input file
    input_file = open(input, 'r')
    jf = input_file.readlines()
    input_file.close()
  
    my_js = []
    #manually check each line
    for line in jf:
        if check_json(line) == -1:
            continue
        temp = check_json(line)   
        
        if rename_title(temp) == -1:
            continue
        else:
            temp = rename_title(temp)
        
        if stand_date(temp) == -1:
            continue
        else:
            temp = stand_date(temp)
            
        if check_author(temp) == -1:
            continue
        else:
            temp = check_author(temp)
            
        if check_count(temp) == -1:
            continue
        else:
            temp = check_count(temp)
            

        temp = slice_tag(temp)
        my_js.append(temp)    

    #write to output file
    with open(output, 'w') as f:
        f.truncate(0)
        for dic in my_js:
            json.dump(dic, f)
            f.write("\n")
        f.close()
    print(f"All cleaned to file: {output}")
    return 0

if __name__ == '__main__':
    main()
