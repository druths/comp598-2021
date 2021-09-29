import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class IPAddrFileTest(unittest.TestCase):
    def setUp(self):
        self.ip_file_path = os.path.join(parentdir, 'ip_address.txt')

    def test_tsv_dataset_file(self):
        print("\nRUNNING TESTS FOR HW4 - ip_address.txt")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.ip_file_path), True)
        print("OK")

        
        with open(self.ip_file_path, 'r', encoding='utf-8') as f:
            print("Check structure - file should contain only one line...")
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            print("OK")

            print("Check structure - string should be an IP address")
            ip_addr = lines[0]
            print(ip_addr)
            self.assertRegex(ip_addr, r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
            print("OK")
        f.close()
        
        print("You are all set! <3")
    
    
if __name__ == '__main__':
    unittest.main()