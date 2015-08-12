__author__ = 'wenzou'
import unittest
from objects import FactorManager

class TestFactoryManager(unittest.TestCase):

    def setUp(self):
        self.factorManager = FactorManager()

    def test_simple_array(self):
        input_list = [10,5, 2, 20]
        return_list = self.factorManager.return_factor(input_list)
        expected_return = {
            10: [5, 2],
            5: [],
            2: [],
            20: [10, 5, 2]
        }
        self.assertEqual(expected_return, return_list)

if __name__ == '__main__':
    unittest.main()
