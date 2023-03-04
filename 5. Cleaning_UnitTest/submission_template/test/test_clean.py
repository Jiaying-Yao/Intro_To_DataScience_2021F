import unittest
from pathlib import Path
import os, sys
import json
from src.clean import check_json, rename_title, stand_date, check_author, check_count, slice_tag

#?? if syntax wrong, fail all tests?
class CleanTest(unittest.TestCase):


    def setUp(self):
        parentdir = Path(__file__).parents[1]
        sys.path.append(parentdir)

        #fixture paths:
        self.fixture1_path = os.path.join(parentdir, 'test', 'fixtures','test_1.json')
        self.fixture2_path = os.path.join(parentdir, 'test', 'fixtures','test_2.json')
        self.fixture3_path = os.path.join(parentdir, 'test', 'fixtures','test_3.json')
        self.fixture4_path = os.path.join(parentdir, 'test', 'fixtures','test_4.json')
        self.fixture5_path = os.path.join(parentdir, 'test', 'fixtures','test_5.json')
        self.fixture6_path = os.path.join(parentdir, 'test', 'fixtures','test_6.json')

        #try on fixtures first:
        #self.output_file_path = os.path.join(parentdir, 'test/fixtures/test_2.json')
        #with open(self.output_file_path, 'r', encoding='utf-8') as f:
            #self.js = json.load(f)
    
    def test_title(self):
        #check fixture1:
        print("\n Fixture1: Checking for title or title_text")
        with open(self.fixture1_path, 'r', encoding = 'utf-8') as f:
            fix1 = f.readline()
            fix1 = json.loads(fix1)
            f.close()
        
        output = rename_title(fix1)
        self.assertEqual(output, -1)
        
        print("OK: clean.py catched title error in fixture1")

    def test_createAt(self):
        #??'2020-10-19T02:56:51+0000' != '2020-10-19T02:56:51+00:00'
        #https://bugs.python.org/issue42371
        #check fixture2:
        print("\n Fixture2: Checking CreatedAt date format")
        with open(self.fixture2_path, 'r', encoding = 'utf-8') as f:
            fix2 = f.readline()
            fix2 = json.loads(fix2)
            f.close()
        output = stand_date(fix2)
        self.assertEqual(output, -1)
        #date = parser.parse(self.js['createdAt'])
        #self.assertIsInstance(date, datetime.date)
        print("OK: clean.py catches CreatedAt error in fixture2")

    def test_json(self):
        print("\n Fixture3: Checking if in the right json format")
        #output_file_path = os.path.join(parentdir, 'test/fixtures/test_2.json')
        with open(self.fixture3_path, 'r', encoding = 'utf-8') as f:
            fix3 = f.readline()
        output = check_json(fix3)
        self.assertEqual(output, -1)
        print("OK: clean.py catched wrong json format of fixture3")
        f.close()
    
    def test_author(self):
        print("\n Fixture4: Checking if author is not empty null or na")
        with open(self.fixture4_path, 'r', encoding = 'utf-8') as f:
            fix4 = f.readline()
            fix4 = json.loads(fix4)
            f.close()
        output = check_author(fix4)
        self.assertEqual(output, -1)
        print("OK: clean.py catched inproper author in fixture4")

    def test_count(self):
        #? castable
        print("\n Fixture5: Checking test_count is an castable integer")
        with open(self.fixture5_path, 'r', encoding = 'utf-8') as f:
            fix5 = f.readline()
            fix5 = json.loads(fix5)
            f.close()
        output = check_count(fix5)
        self.assertEqual(output, -1)
        print("OK: clean.py catched uncastable test_count in fixture5")

    def test_tags(self):
        print("\n Fixture6: Checking if tags can be properly splited")
        with open(self.fixture6_path, 'r', encoding = 'utf-8') as f:
            fix6 = f.readline()
            fix6 = json.loads(fix6)
            f.close()
        output = slice_tag(fix6)
        tag_detected = output['tags']
        tag_expected = " ".join(fix6['tags']).split()
        self.assertCountEqual(tag_detected,tag_expected)
        print("OK: clean.py splitted the tags in fixture6")
        


        
    
if __name__ == '__main__':
    unittest.main()