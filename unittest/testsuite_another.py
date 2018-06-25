import unittest
import sys
import os
sys.path.append(os.getcwd())

from testsuite_oneclass import Example

def mul(a, b):
    return a * b

class Multiple(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "Enter setUpClass"
 
    @classmethod
    def tearDownClass(self):
        print "Enter tearDownClass"
 
    def setUp(self):
        print self._testMethodName

    def tearDown(self):
        print self._testMethodName

    def test_3(self):
        self.assertEqual(2,mul(1,2))

    def test_4(self):
        self.assertTrue(4 == mul(1,2))

if __name__ == "__main__":
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(Multiple))
   suite.addTest(unittest.makeSuite(Example))
   run = unittest.TextTestRunner()
   run.run(suite)
