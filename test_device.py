import unittest
from unittest.mock import patch
from device import dvc

class TestDevice(unittest.TestCase):
    @patch('builtins.input', return_value='')
    def test1(self, mock_input):
        print("Test 1: Empty input")
        result = dvc()
        self.assertEqual(result, 'Locked')
        
    @patch('builtins.input', return_value='817341')
    def test2(self, mock_input):
        print("Test 2: Input with only unlock code")
        result = dvc()
        self.assertEqual(result, 'Unlocked')
        
    @patch('builtins.input', return_value='sdfjid33j33n3m32ds0fdsi0fi')
    def test3(self, mock_input):
        print("Test 3: Input of letters and numbers")
        result = dvc()
        self.assertEqual(result, 'Locked')
        
    @patch('builtins.input', return_value='817341298349843981734434878347817341')
    def test4(self, mock_input):
        print("Test 4: Input with unlock, lock, then unlock code, with numbers in between")
        result = dvc()
        self.assertEqual(result, 'Unlocked')
    
    @patch('builtins.input', return_value='1')
    def test5(self, mock_input):
        print("Test 5: Input with only 1 number")
        result = dvc()
        self.assertEqual(result, 'Locked')
        
if __name__ == '__main__':
   unittest.main()