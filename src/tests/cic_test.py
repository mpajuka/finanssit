import unittest
from compound_interest_calc import calculate_investments, format_input


class CicTest(unittest.TestCase):
    def setUp(self):
        self.curr_value = 1000
        self.cont = 100
        self.r = 7
        self.t = 10

    def test_cic_final_sum(self):
        self.assertEqual(int(calculate_investments(
            self.curr_value, self.cont, self.r, self.t, True)), 18546)

    def test_cic_with_string(self):
        self.assertEqual(int(format_input("1000", "100", "7", "10", True)), 18546)
