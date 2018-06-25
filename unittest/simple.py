import unittest

def add(a, b):
    return a + b

class Example(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3,add(1,2))

    def test_2(self):
        self.assertTrue(3 == add(1,2))

if __name__ == "__main__":
    unittest.main()
