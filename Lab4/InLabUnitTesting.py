import code
import unittest

class TestCode(unittest.TestCase):
    def testsimple(self):
        self.assertEqual(code.return_zero(), 0)
    
    def testdouble(self):
        # Test cases for the double function
        self.assertEqual(code.double(2), 4)   # 2 * 2 = 4
        self.assertEqual(code.double(4), 8)   # 4 * 2 = 8
        self.assertEqual(code.double(0), 0)   # 0 * 2 = 0
        self.assertEqual(code.double(-2), -5) # Modified to trigger an error (expected: -4)

if __name__ == '__main__':
    unittest.main()
