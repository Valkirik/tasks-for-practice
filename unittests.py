import unittest
from list_int import two_num
from anagramma import compresed_string

class MyTests(unittest.TestCase):
    def for_two_num(self):
        #arrange
        l = [1, 2, 3, 4, 5]
        n = 9
        #act
        result = two_num(l, n)
        #assert
        self.assertEqual(result, [4, 5])\

    def for_anagramma(self):
        #arrange
        string = "AaabBccdddee"

        #act
        result = compresed_string(string)

        #assert
        self.assertEqual(result, "a3b2c2d3e2")

if __name__ == "__main__":
    unittest.main()