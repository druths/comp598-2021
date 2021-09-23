import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class StatTest(unittest.TestCase):
    def setUp(self):
        self.stats_file_path = os.path.join(parentdir, 'scripts', 'stats.sh')

    def test_tsv_dataset_file(self):
        print("\nRUNNING TESTS FOR HW3 - stats.sh")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.stats_file_path), True)
        print("OK")

        
        with open(self.stats_file_path, 'r', encoding='utf-8') as f:
            print("Check structure - script starts with #!/bin/bash")
            lines = f.readlines()
            bashscrp = lines[0].strip()

            self.assertEqual(bashscrp, "#!/bin/bash")
            print("OK")
        f.close()
        
        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()