import unittest


class TestClass07(unittest.TestCase):
    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case01()")




        """
        run this code with following format in terminal:
        $ python -m unittest test_module6 -v
        """