import unittest
import langevin
import numpy as np
from langevin import my_dynamics


class Test(unittest.TestCase):

    # Testing the standard deviation
    def test_std_dev(self):
        result1 = langevin.std_dev(1,50,1)
        self.assertEqual(result1, 10)

    #testing the number of steps
    def test_num_steps(self):
        result2 = langevin.num_steps(1,0.1)
        self.assertEqual(result2, 10)

if __name__ == '__main__':
    unittest.main() 
