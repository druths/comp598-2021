import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class FilesExistTest(unittest.TestCase):
    def setUp(self):
        self.collect_file_path = os.path.join(parentdir, 'src', 'build_interaction_network.py')
        self.compute_title_lengths_file_path = os.path.join(parentdir, 'src', 'compute_network_stats.py')
        
        self.sample1_file_path = os.path.join(parentdir, 'interaction_network.json')
        self.sample2_file_path = os.path.join(parentdir, 'stats.json')
        
        print("\nRUNNING TESTS FOR HW7")

    def test_collect(self):
        print(f"Ensure build_interaction_network.py file exists")
        self.assertEqual(os.path.isfile(self.collect_file_path), True)
        print("OK")

        
    def test_extract_to_tsv(self):
        print(f"Ensure compute_network_stats.py file exists")
        self.assertEqual(os.path.isfile(self.compute_title_lengths_file_path), True)
        print("OK")

    
    def test_data_files_exist(self):    
        print(f"Ensure all the required data files are present files exist")
        self.assertEqual(os.path.isfile(self.sample1_file_path), True)
        self.assertEqual(os.path.isfile(self.sample2_file_path), True)
        print("OK")

    def tearDownClass():
        print("\n\nYou are all set! <3")
    
if __name__ == '__main__':
    unittest.main()