import unittest

def add(a, b):
    return a + b

class Example(unittest.TestCase):
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

    def test_1(self):
        self.assertEqual(3,add(1,2))

    def test_2(self):
        self.assertTrue(3 == add(1,2))

class Example2(unittest.TestCase):
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
        self.assertEqual(5,add(2,3))

    def test_4(self):
        self.assertTrue(5 == add(2,3))

if __name__ == "__main__":
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(Example))
   suite.addTest(unittest.makeSuite(Example2))
   run = unittest.TextTestRunner()
   run.run(suite)
