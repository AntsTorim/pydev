'''
Created on 19.07.2013

@author: Ants Torim
'''
import unittest
from tabel import Tabel


class Test(unittest.TestCase):


    def testName(self):
        t = Tabel(4, 5)
        t[0][0] = 1
        self.assertEquals(t[0][0], 1)
        self.assertEquals(t[0][1], 0)
        self.assertEqual(t.freq[0][0], 3)
        self.assertEqual(t.freq[0][1], 1)
        self.assertEqual(t.weight[0][0], 16)
        self.assertEqual(t.weight[0][1], 1)
        self.assertEqual(t.weight[1][0], 19)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()