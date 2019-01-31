#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:42:04 2019

@author: Fabiana
"""

###########################################


# CHAPTER 4 - INTRODUCTION TO UNIT TESTING


##########################################

# Functions file



#----------------------------------------
# Task 1 - Prime numbers
#----------------------------------------

# In the example below I need to write a function to check if an input number is a prime number. The function will not pass the test.


#def is_prime(number):
#    """Return True if *number* is prime."""
#    for element in range(number): 
#        if number % element == 0:
#            return False 
#    return True
#
#def print_next_prime(number):
#    """Print the closest prime number larger than *number*."""
#    index = number 
#    while True:
#        index += 1
#        if is_prime(index):
#            print(index)
            
#----------------------------------------
# Task 2 - Prime numbers second version
#----------------------------------------   
            
# In this task I'm writing the code in order to pass the test
            
#def is_prime(number):
#    """Return True if *number* is prime.""" 
#    if number < 0:
#        return False
#    if number in (0, 1):
#        return False
#    for element in range(2, number):
#        if number % element == 0:
#            return False
#    return True    


#----------------------------------------
# Task 3 - Prime numbers third version
#----------------------------------------  

# Below I'm rewriting the same function by improving it
    
def is_prime(number):
    """Return True if *number* is prime.""" 
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True 
