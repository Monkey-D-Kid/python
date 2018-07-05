import unittest
import simple
from simple import Add, Multiple

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Add))
suite.addTest(unittest.makeSuite(Multiple))

testLoad = unittest.TestLoader()
suite_Add = testLoad.loadTestsFromTestCase(Add)
suite_Mul = testLoad.loadTestsFromTestCase(Multiple)
suite_list = unittest.TestSuite([suite_Add, suite_Mul])

suite_module = testLoad.loadTestsFromModule(simple)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
print "List"
runner.run(suite_list)
print "Module"
runner.run(suite_module)
