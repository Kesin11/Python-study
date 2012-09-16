import unittest

class Test(unittest.TestCase):
    def test_almost_eq(self):
        a = 12.11234
        b = 12.11233
        self.assertAlmostEquals(a, b, places=4)
        

if __name__ == '__main__':
    unittest.main()