import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class FilesExistTest(unittest.TestCase):
    def setUp(self):
        self.collect_file_path = os.path.join(parentdir, 'src', 'collect_newest.py')
        self.compute_title_lengths_file_path = os.path.join(parentdir, 'src', 'extract_to_tsv.py')
        self.collect_relationships_file_path = os.path.join(parentdir, 'src', 'analyze.py')
        self.sample1_file_path = os.path.join(parentdir, 'concordia.json')
        self.sample2_file_path = os.path.join(parentdir, 'mcgill.json')
        self.annotated_mcgill = os.path.join(parentdir, 'annotated_mcgill.tsv')
        self.annotated_concordia = os.path.join(parentdir, 'annotated_concordia.tsv')
        print("\nRUNNING TESTS FOR HW7")

    def test_collect(self):
        print(f"Ensure collect_newest.py file exists")
        self.assertEqual(os.path.isfile(self.collect_file_path), True)
        print("OK")

        
    def test_extract_to_tsv(self):
        print(f"Ensure extract_to_tsv.py file exists")
        self.assertEqual(os.path.isfile(self.compute_title_lengths_file_path), True)
        print("OK")

    def test_analyze(self):
        print(f"Ensure analyze.py file exists")
        self.assertEqual(os.path.isfile(self.collect_relationships_file_path), True)
        print("OK")
    
    def test_data_files_exist(self):    
        print(f"Ensure all the required data files are present files exist")
        self.assertEqual(os.path.isfile(self.sample1_file_path), True)
        self.assertEqual(os.path.isfile(self.sample2_file_path), True)
        self.assertEqual(os.path.isfile(self.annotated_mcgill), True)
        self.assertEqual(os.path.isfile(self.annotated_concordia), True)
        print("OK")

    def tearDownClass():
        print("\n\nYou are all set! <3")
    
if __name__ == '__main__':
    unittest.main()