import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)

class StatsTest(unittest.TestCase):
    def setUp(self):
        self.stats_file_path = os.path.join(parentdir, 'stats.sh')

    def test_stats_file(self):
        print("\nRUNNING TESTS FOR HW2 - stats.sh")
        print("Ensure stats file exists")
        self.assertEqual(os.path.isfile(self.stats_file_path), True)
        print("OK")
        print("Check header for #!/bin/bash - ensure the first line is like that")
        with open(self.stats_file_path, 'r', encoding='utf-8') as f:
            bashbang = f.readline()
            self.assertEqual(bashbang.strip(), ('#!/bin/bash'))
        f.close()
        
        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()