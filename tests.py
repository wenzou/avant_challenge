__author__ = 'wenzou'
import unittest
from objects import FactorManager, CreditLine

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

    def test_empty_array(self):
        input_list = []
        return_list = self.factorManager.return_factor(input_list)
        expected_return = {}
        self.assertEqual(expected_return, return_list)

    def test_repeating_array(self):
        input_list = [20,20, 2, 20, 20]
        return_list = self.factorManager.return_factor(input_list)
        expected_return = {
            20: [2],
            2: [],
        }
        self.assertEqual(expected_return, return_list)

    def test_caching_array(self):
        self.factorManager = FactorManager(cache=True)
        input_list = [10,5, 2, 20]
        return_list = self.factorManager.return_factor(input_list)
        expected_return = {
            10: [5, 2],
            5: [],
            2: [],
            20: [10, 5, 2]
        }
        self.assertEqual(expected_return, return_list)
        return_list = self.factorManager.return_factor(input_list)
        self.assertEqual(expected_return, return_list)

class TestCreditLine(unittest.TestCase):

    def setUp(self):
        self.creditLine = CreditLine()

    def test_cases_1(self):
        self.creditLine = CreditLine(35.0)
        self.creditLine.draw_credit(500)
        self.creditLine.advance_days(30)
        return_amount = self.creditLine.get_balance()
        expected_return = 514.38
        self.assertEqual(expected_return, return_amount)

    def test_cases_2(self):
        self.creditLine = CreditLine(35.0)
        self.creditLine.draw_credit(500)
        self.creditLine.advance_days(15)
        self.creditLine.make_payment(200)
        self.creditLine.advance_days(10)
        #print self.creditLine.interest_charge
        self.creditLine.draw_credit(100)
        self.creditLine.advance_days(5)
        #print self.creditLine.interest_charge

        return_amount = self.creditLine.get_balance()
        expected_return = 411.99
        self.assertEqual(expected_return, return_amount)

    def test_cases_3(self):
        self.creditLine = CreditLine(35.0)
        self.creditLine.draw_credit(500)
        self.creditLine.advance_days(45)

        return_amount = self.creditLine.get_balance()
        expected_return = 514.38
        excepted_current_interest = 7.3986676674798275
        self.assertEqual(expected_return, return_amount)
        self.assertEqual(excepted_current_interest, self.creditLine.interest_charge)

    def test_cases_4(self):
        self.creditLine = CreditLine(35.0)
        self.creditLine.draw_credit(500)
        self.creditLine.advance_days(120)

        return_amount = self.creditLine.get_balance()
        expected_return = 560.06
        self.assertEqual(expected_return, return_amount)

if __name__ == '__main__':
    unittest.main()
