##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Wed Jan 23 10:00:33 2019
#
#@author: Fabiana
#"""
#
####################################
#
## CHAPTER 02 - VALIDATION
#
####################################
#
## To check and validate user input. For example what happens on a form when the user is typing the wrong data input: a string instead of a number.
#
##----------------------------------
## Task 01 - Revise input function
##----------------------------------
#
## Ask user input with a pre-coded new line or with a space in front
#
## With a new line
#print ("What’s your age?")
#Age = input()
#
## With a space
#Age = input("What’s your age? ")
#
##-----------------------------------------------------------------
## Task 02 - Cast the previous coding example age to int data type
##----------------------------------------------------------------
#
#print ("What’s your age?")
#age = int(input()) # By adding int I make sure that the input is an integer number
#print (type(age)) # type function to check if I have successfully cast the data into the correct data type!
#
#age = int(input("What’s your age? ")) # In this way I'm using just a line of code and I can save space (memory).
#
#
#
##-----------------------------------------------------
## Task 03 - An example for validating string content
#
#option = input("Please input yes or no ").lower()
#
#print(option)
#
#
##---------------------------------------------------
## Task 04 - An example for validating string lenght
##---------------------------------------------------
#
#
#userInput = input('Type your phone number: ')
#
#if len(userInput) > 12:
#    print('Too long. Please check again, the maximum lenght is 12 digits.')
#elif len(userInput) == 0:
#    print('Please type your phone number.')
#elif len(userInput) <= 9:
#    print('Too short. Please check again, the minimum lenght is 9 digits.')   
#    
#    
##-----------------------------------------------------------------
## Task 05 - Arrange the code in a correct logical order and run it
##-----------------------------------------------------------------

print('***choice****')
print('1. Display my name')
print('2. Display my age')
print('3. Display my city')


choice = 0

#while choice < 1 or choice > 3: 
#    choice = int(input('What is your choice? '))
#    
##if choice >= 4:
##    print('Chose options: 1, 2 or 3')
#if choice == 1:
#    print('Ms Wu')
#elif choice == 2:
#    print('5 years old')
#elif choice == 3: 
#    print('London')    


# In the example above in the while I'm setting that the options can only be between 1 and 3. In fact, if I answer any other number to the question: "What is your choice?" I just keep seeing the same question without any other suggestions for the user. In the last elif I added a sentence to give a suggestion to the user, but that condition is never met because in the while loop I'm stating that the choice is between 1 and 3.
    
    
#--------------------------------------
# Task 06 - Handling errorful input 
#--------------------------------------
    
# How to give suggestions to the user other than ask for an input 

#    
while True:
    try:
        while (choice < 1) or (choice > 3):
            print('please type a number between 1 and 3')
            choice = int(input('What is your choice?'))
        break
    except ValueError:
        print('please, type a number')
        
if choice == 1:
    print('Ms Wu')
elif choice == 2:
    print('5 years old')
elif choice == 3: 
    print('London')


#try:
#    while choice < 1 or choice > 3:
#        print('please type a number between 1 and 3')
#        choice = int(input('What is your choice?'))
#     
#except ValueError:
#    print('please, type a number')
#    choice = int(input('What is your choice?'))
#       
#else:
#    if choice == 1:
#        print('Ms Wu')
#    elif choice == 2:
#        print('5 years old')
#    elif choice == 3: 
#        print('London')
