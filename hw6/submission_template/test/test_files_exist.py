import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class FilesExistTest(unittest.TestCase):
    def setUp(self):
        self.collect_file_path = os.path.join(parentdir, 'src', 'collect.py')
        self.compute_title_lengths_file_path = os.path.join(parentdir, 'src', 'compute_title_lengths.py')
        self.collect_relationships_file_path = os.path.join(parentdir, 'src', 'collect_relationships.py')
        self.sample1_file_path = os.path.join(parentdir, 'sample1.json')
        self.sample2_file_path = os.path.join(parentdir, 'sample2.json')
        print("\nRUNNING TESTS FOR HW6")

    def test_collect(self):
        print(f"Ensure collect.py file exists")
        self.assertEqual(os.path.isfile(self.collect_file_path), True)
        print("OK")

        
    def test_compute_title_lengths(self):
        print(f"Ensure compute_title_lengths.py file exists")
        self.assertEqual(os.path.isfile(self.compute_title_lengths_file_path), True)
        print("OK")

    def test_collect_relationships(self):
        print(f"Ensure collect_relationships.py file exists")
        self.assertEqual(os.path.isfile(self.collect_relationships_file_path), True)
        print("OK")
    
    def test_samples_exist(self):    
        print(f"Ensure sample1.json and sample2.json files exist")
        self.assertEqual(os.path.isfile(self.sample1_file_path), True)
        self.assertEqual(os.path.isfile(self.sample2_file_path), True)
        print("OK")

    def tearDownClass():
        print("\n\nYou are all set! <3")
    
if __name__ == '__main__':
    unittest.main()