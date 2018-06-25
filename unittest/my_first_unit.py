#!/usr/bin/env python

import unittest

class MyTest(unittest.TestCase):

  def test_equal(self):
    self.assertEqual(3, 6/2)

  def test_CAP(self):
    self.assertEqual("abc".upper(), "ABCD")

if __name__ == "__main__":
#  unittest.main()
  suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
  unittest.TextTestRunner(verbosity=2).run(suite)
