'''
Created on 19.07.2013

@author: Ants Torim
'''
import unittest
from tabel import Tabel, KaalutudTabel


class Test(unittest.TestCase):


    def testSimple(self):
        t = Tabel(4, 5)
        t[0][0] = 1
        self.assertEquals(t[0][0], 1)
        self.assertEquals(t[0][1], 0)
        self.assertEqual(t.freq[0][0], 3)
        self.assertEqual(t.freq[0][1], 1)
        self.assertEqual(t.weight[0], 17)
        self.assertEqual(t.weight[1], 19)
    
    def testWeighted(self):
        t = KaalutudTabel(4, 5, [2, 1, 1, 1])
        t[0][0] = 1
        print(t.freq)
        self.assertEqual(t.freq[0][0], 3)
        self.assertEqual(t.freq[0][1], 2)
        self.assertEqual(t.weight[0], 22)
        self.assertEqual(t.weight[3], 23)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()