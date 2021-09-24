import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
import pandas as pd


class DatasetTest(unittest.TestCase):
    def setUp(self):
        self.dataset_file_path = os.path.join(parentdir, 'dataset.tsv')

    def test_tsv_dataset_file(self):
        print("\nRUNNING TESTS FOR HW1 - dataset.tsv")
        print("Ensure dataset.tsv exists")
        self.assertEqual(os.path.isfile(self.dataset_file_path), True)
        print("OK")

        print("Check header")
        with open(self.dataset_file_path, 'r', encoding='utf-8') as f:
            header = f.readline()
            self.assertEqual(header.startswith("tweet_id"), True)
        f.close()
        df = pd.read_csv(self.dataset_file_path, sep='\t')
        cols = list(df.columns)
        self.assertEqual(len(cols), 4)
        self.assertEqual(cols[0], 'tweet_id')
        self.assertEqual(cols[1], 'publish_date')
        self.assertEqual(cols[2], 'content')
        self.assertEqual(cols[3], 'trump_mention')
        print("OK")
        
        print("Check file contents")
        df = pd.read_csv(self.dataset_file_path, sep='\t')
        self.assertEqual((len(df.index) > 5), True)
        print("OK")

        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()