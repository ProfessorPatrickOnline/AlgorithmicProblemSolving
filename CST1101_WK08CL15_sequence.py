# -*- coding: utf-8 -*-
"""
This program only works with an integer argument.
Created for CST1101 Spring 2021, Week#08 Class#15.
This example program demonstrates an unproven loop.

Created on Tue 23-Mar-2021.
@author: ProfessorPatrick.
"""

# There is no proof that this loop must always end 

def sequence(n=3):
    while n != 1:
        print(n),
        if n % 2 == 0:        # n is even
            n = int(n / 2)
        else:                 # n is odd
            n = n * 3 + 1

# Trace the values of n and the output for each state of execution
