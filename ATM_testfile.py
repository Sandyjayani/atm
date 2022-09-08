from unittest import TestCase, mock
import unittest

from hw_4 import verify_pin, check_input, transaction
#import locally functions to test

class ATM_test(unittest.TestCase):

#1.test withdrawl works
    def test_correct_withdrawal(self):
        result = transaction(withdraw=20)
        self.assertEqual(result, 80)


#2.test if withdrawal doesn't not work
    def test_incorrect_withdrawal(self):
        result = transaction(withdraw=350)
        self.assertEqual(result, 100)


#3.check correct pin is recognised
    def test_correct_pin(self):
        a = verify_pin(pin=1111)
        self.assertTrue(a)


#4.test if incorrect pin is recognised
    def test_incorrect_pin(self):
        a = verify_pin(pin=1234)
        self.assertEqual(a, False)

    
#5.test if input is a number
    def test_input_is_number(self):
        a = check_input(withdraw="a")
        self.assertEqual(a, False)

#6.test if input is a negative number
    def test_input_is_negative(self):
        a = check_input(withdraw=-20)
        self.assertEqual(a, False)

#7.test if input is a positive number
    def test_input_is_positive(self):
        a = check_input(withdraw=20)
        self.assertEqual(a, True)
    
#8.test if input is a zero
    def test_input_is_zero(self):
        a = check_input(withdraw=0)
        self.assertEqual(a, False)

# -- unit test --

if __name__ == '__main__':
    unittest.main(verbosity= 2)

