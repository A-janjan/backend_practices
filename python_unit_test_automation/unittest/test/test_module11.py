import unittest


class TestClass12(unittest.TestCase):
    def test_case01(self):
        """This is a test method..."""
        print(self.id())
        self.fail()

    
    def test_case02(self):
        """This is a another test method..."""
        print(self.id())
        print("why?")