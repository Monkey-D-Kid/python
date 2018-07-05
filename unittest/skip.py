import unittest

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

@unittest.skip("Skip the whole class")
class Add(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3,add(1,2))

    def test_2(self):
        self.assertTrue(3 == add(1,2))

class Multiple(unittest.TestCase):
    def test_3(self):
	self.assertEqual(4, mul(2,2))

#    @unittest.skip("Intentionally skip")
#    @unittest.expectedFailure
    def test_4(self):
	self.assertEqual(4, mul(1,2))

if __name__ == "__main__":
    unittest.main()
