import unittest

class TestClass1(unittest.TestCase):
    def test_case1(self):
        my_str = 'amir'
        my_int = 987
        self.assertTrue(isinstance(my_str, str))
        self.assertTrue(isinstance(my_int, int))
        
    def test_case2(self):
        my_pi = 3.14
        self.assertFalse(isinstance(my_pi, int))
        

if __name__ == "__main__":
    unittest.main()