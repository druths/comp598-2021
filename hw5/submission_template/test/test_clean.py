import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class CleanTest(unittest.TestCase):
    # def setUp(self):
        # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.
        

    # def test_title(self):
        # Just an idea for a test; write your implementation
        
    
if __name__ == '__main__':
    unittest.main()