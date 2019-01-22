#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:03:57 2019

@author: Fabiana
"""

########################################

# CHAPTER 01 - EXCEPTIONS

#######################################

#------------------------------
# Task 01 - Error message
#------------------------------

#f = open('testfile')
#If I run  the code above,I'll receive a general error saying: there isn't any file or directory with this name.

try:
    f = open('testfile')
except Exception: 
    print('Error!')
#By using try and except we can give more information about the error. In this example we'll read: Error!    

#print()
#try:
#    f = open('testfile') 
#except Exception:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
# In this example I'm giving more information about the error. The purpose is be as much informative as possible in order to fix the error in the quicker way possible.

#try:
#    f = open('testfile.txt')
#except Exception: 
#    print('Error!')    
    

    
#------------------------------
# Task 02 - Multiple errors
#------------------------------  
    
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit 
#except Exception:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
# Here finally the file name is complete and correct, but I have a new error linked to the variable name. However, the error message in the console is going to say the same thing and it's not useful anymore. I need to find another way.
    
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.') 
# FileNotFoundError is a built in Exceptions. By using it I can spot and differentiate the error messages.    
   
#print()    
#try:
#    f = open('testfil.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
#except Exception:
#    print('Sorry. Something is wrong after opening function.')
    

#-------------------------------------------
# Task 03 - Print out exception as detected
#------------------------------------------

#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except Exception as e:
#    print(e)     

#-------------------------------------------
# Task 04 - Else block ??????????????
#------------------------------------------

#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e) 
#else:
#    print(f.read()) 
#    f.close()    
    
    
#-------------------------------------------
# Task 05 - Finally block
#------------------------------------------    
    
#The finally clause will run regardless of what happens in the try/except block. The finally block is useful to go trough the program even if there are errors and close it.

#try:
#    f = open('testfile')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print('executing finally...')  
# Above I tried a function with an error in the name of the file after "open"

#try:
#    f = open('testfile.txt')
#except Exception as e: 
#    print(e)
#else:
#    print(f.read())
#    f.close() 
#finally:
#    print('executing finally...') 
# Above I tried a fuction without any error

#-------------------------------------------
# Task 06 - manually raise an exception
#------------------------------------------   
    
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt': 
        raise Exception
except Exception as e:
    print('file name are the same')
    
print()
try:
    with open('test.txt', 'r') as f:
#        f_text = str('not equal')
        if f.name == 'testfile.txt':
            # it's better to raise specific errors than generic
            print('same file')
except Exception:
    raise OSError('that is the wrong file')
#else:
#    print(f_text)
finally:
    print('this is the end!')    