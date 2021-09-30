import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class IPAddrFileTest(unittest.TestCase):
    def setUp(self):
        self.ip_file_path = os.path.join(parentdir, 'jupyter.log')

    def test_tsv_dataset_file(self):
        print("\nRUNNING TESTS FOR HW4 - jupyter.log")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.ip_file_path), True)
        print("OK")
        
        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()