#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:50:38 2019

@author: Fabiana
"""

###########################################


# CHAPTER 4 - INTRODUCTION TO UNIT TESTING


##########################################


# Test file - Where I'm testing the functions contained in ch04_Fabiana.py file


import unittest
from ch04_Fabiana import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""
    def test_is_five_prime(self): #The method's name has to start with "test" otherwise the test is not going to work.
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__': 
    unittest.main()
    
    