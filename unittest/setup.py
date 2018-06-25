import unittest

def add(a, b):
    return a + b

class Example(unittest.TestCase):
#2   @classmethod
#2   def setUpClass(self):
#2       print "Enter setUpClass"
#2
#2   @classmethod
#2   def tearDownClass(self):
#2       print "Enter tearDownClass"
#1
#1    def setUp(self):
#1        print self._testMethodName
#1
#1    def tearDown(self):
#1        print self._testMethodName

    def test_1(self):
        self.assertEqual(3,add(1,2))

    def test_2(self):
        self.assertTrue(3 == add(1,2))

if __name__ == "__main__":
    unittest.main()
