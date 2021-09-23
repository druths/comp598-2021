import unittest
from pathlib import Path
import os, sys
import json
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class OutputTest(unittest.TestCase):
    def setUp(self):
        self.output_file_path = os.path.join(parentdir, 'output.json')

    def test_tsv_dataset_file(self):
        print("\nRUNNING TESTS FOR HW3 - output.json")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.output_file_path), True)
        print("OK")

        with open(self.output_file_path, 'r', encoding='utf-8') as f:
            results = json.load(f)
            print("Ensure both keys, count and verbosity, are present")
            self.assertCountEqual(list(results.keys()), ['count', 'verbosity'])
            print("OK")

            print("Ensure keys for count are correct")
            keys = ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy"]
            key_count_in_file = results.get("count", {}).keys()
            self.assertCountEqual(list(key_count_in_file), keys)
            print("OK")

            print("Ensure keys for verbosity are correct")
            key_verbosity_in_file = results.get("verbosity", {}).keys()
            self.assertCountEqual(list(key_verbosity_in_file), keys)
            print("OK")
        f.close()

        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()