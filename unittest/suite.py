import unittest
import AddSub
import MulDiv

suite = unittest.TestSuite()
suite.addTest(AddSub.AddSub("test_add"))
suite.addTest(AddSub.AddSub("test_sub"))

loader = unittest.TestLoader()
new_suite = loader.loadTestsFromModule(MulDiv)

test_suite = unittest.TestSuite(suite)
runner = unittest.TextTestRunner()
runner.run(test_suite)
