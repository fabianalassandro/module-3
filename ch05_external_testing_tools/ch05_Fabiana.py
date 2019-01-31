#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:08:04 2019

@author: Fabiana
"""

#########################################

# CHAPTER 5 - EXTERNAL TESTING TOOLS

########################################

# Functions file to test

class Calculator(object):
#    def add(self, x, y):
#        number_types = (int, float, complex)
#        if isinstance(x, number_types) and isinstance(y, number_types):
#            return x+y
#        else:
#            raise ValueError

    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb; pdb.set_trace() # New debugginf technique
            result = x - y
            print('Result is: {}'.format(result))
            return result
        else:
            raise ValueError