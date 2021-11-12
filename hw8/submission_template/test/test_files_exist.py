import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class FilesExistTest(unittest.TestCase):
    def setUp(self):
        self.collect_file_path = os.path.join(parentdir, 'src', 'compile_word_counts.py')
        self.compute_title_lengths_file_path = os.path.join(parentdir, 'src', 'compute_pony_lang.py')
        self.collect_relationships_file_path = os.path.join(parentdir, 'test', 'test_tasks.py')
        self.sample1_file_path = os.path.join(parentdir, 'word_counts.json')
        
        print("\nRUNNING TESTS FOR HW8")

    def test_word_count(self):
        print(f"Ensure compile_word_counts.py file exists")
        self.assertEqual(os.path.isfile(self.collect_file_path), True)
        print("OK")

        
    def test_compute_lang(self):
        print(f"Ensure compute_pony_lang.py file exists")
        self.assertEqual(os.path.isfile(self.compute_title_lengths_file_path), True)
        print("OK")

    def test_file_test(self):
        print(f"Ensure test_tasks.py file exists")
        self.assertEqual(os.path.isfile(self.collect_relationships_file_path), True)
        print("OK")
    
    def test_data_files_exist(self):    
        print(f"Ensure all the required data files are present files exist")
        self.assertEqual(os.path.isfile(self.sample1_file_path), True)
        print("OK")

    def tearDownClass():
        print("\n\nYou are all set! <3")
    
if __name__ == '__main__':
    unittest.main()