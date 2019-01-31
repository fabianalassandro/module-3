#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:44:42 2019

@author: Fabiana
"""

#########################################

# CHAPTER 5 - EXTERNAL TESTING TOOLS

########################################

#TESTING FILE

import unittest
from ch05_Fabiana import Calculator

class TddInPythonExample(unittest.TestCase):
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
        
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', '3')
        
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, '2', 'three')    
        
if __name__ == '__main__':
    unittest.main()

        