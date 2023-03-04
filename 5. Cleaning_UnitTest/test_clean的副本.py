import unittest
from pathlib import Path
import os, sys
import json
import datetime
import pytz
import dateutil.parser as parser

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)

#?? if syntax wrong, fail all tests?
class CleanTest(unittest.TestCase):
    def test_json(self):
        print("Checking if in the right json format")
        output_file_path = os.path.join(parentdir, 'test/fixtures/test_2.json')
        with open(self.output_file_path, 'r', encoding='utf-8') as f:
            js = json.load(f)
        print("OK")


    def setUp(self):
        #try on fixtures first:
        self.output_file_path = os.path.join(parentdir, 'test/fixtures/test_2.json')
        with open(self.output_file_path, 'r', encoding='utf-8') as f:
            self.js = json.load(f)
    
    def test_title(self):
        print("\n Checking each json has title or title_text")

        #key_title_in_file = [s for s in list(self.js.keys()) if "title" in s]
        #print(key_title_in_file)
        self.assertTrue('title' in list(self.js.keys()) or 'title_text' in list(self.js.keys()))
        
        print("OK")

    def test_createAt(self):
        #??'2020-10-19T02:56:51+0000' != '2020-10-19T02:56:51+00:00'
        #https://bugs.python.org/issue42371
        print("\n Checking if createAt is of form date:")
        date = parser.parse(self.js['createdAt'])
        self.assertIsInstance(date, datetime.date)
        print("OK")

        print("\n Checking if createAt is in form of iso")
        iso1 = date.astimezone(pytz.utc).isoformat()
        iso2 = iso1[:-len('+00:00')] + '+0000'
        self.assertTrue(self.js['createdAt'] == iso1 or self.js['createdAt'] == iso2)
        print("OK")

    def test_author(self):
        print("Checking no author is empty null or na")
        try:
            author = self.js['author']
            self.assertNotIn(author, ["N/A","null",None,""])
            print("OK")
        except KeyError as err:
            print("OK")

    def test_count(self):
        #? castable
        print("Checking test_count is an integer")
        try:
            count = self.js['total_count']
            self.assertIsInstance(count, int)
            print("OK")
        except KeyError as err:
            print("OK")

    def test_tags(self):
        print("Checking if tags is properly splited")
        try:
            tags = self.js['tags']
            split = " ".join(tags).split()
            self.assertEqual(tags, split)
            print("OK")
        except KeyError as err:
            print("OK")
        


        
    
if __name__ == '__main__':
    unittest.main()