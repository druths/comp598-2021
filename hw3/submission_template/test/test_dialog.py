import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class DialogTest(unittest.TestCase):
    def setUp(self):
        self.dialog_file_path = os.path.join(parentdir, 'src', 'dialog_analysis.py')

    def test_tsv_dataset_file(self):
        print("\nRUNNING TESTS FOR HW3 - dialog_analysis.py")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.dialog_file_path), True)
        print("OK")

        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()