import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
import pandas as pd

class ResultsTest(unittest.TestCase):
    def setUp(self):
        self.dataset_file_path = os.path.join(parentdir, 'results.tsv')

    def test_tsv_results_file(self):
        print("\nRUNNING TESTS FOR HW1 - results.tsv")
        print("Ensure results.tsv exists")
        self.assertEqual(os.path.isfile(self.dataset_file_path), True)
        print("✅")
        print("Check header")
        with open(self.dataset_file_path, 'r') as f:
            header = f.readline()
            if header.startswith("result") or header.startswith("\t"):
                startFlag = True
            self.assertEqual(startFlag, True)
        f.close()
        df = pd.read_csv(self.dataset_file_path, sep='\t')
        cols = list(df.columns)
        self.assertTrue(len(cols) in [2, 3])
        if len(cols) == 2:
            self.assertEqual(cols[0], 'result')
            self.assertEqual(cols[1], 'value')
        else:
            self.assertEqual(cols[0], 'Unnamed: 0')
            self.assertEqual(cols[1], 'result')
            self.assertEqual(cols[2], 'value')
        print("✅")
        
        print("Check file contents")
        df = pd.read_csv(self.dataset_file_path, sep='\t')
        self.assertEqual((len(df.index) == 1), True)
        print("✅")

        print("You are all set! 💜")
    
    
if __name__ == '__main__':
    unittest.main()