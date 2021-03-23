# -*- coding: utf-8 -*-
"""
This program only works with an integer argument.
Created for CST1101 Spring 2021, Week#08 Class#15.
Use this program for your state table assignment.

Created on Tue 23-Mar-2021.
@author: ProfessorPatrick.
"""

# You may want to add scaffolding to the program
# Such as a print of n, count, and digit
def num_zero_and_five_digits(n=1055030250):
    count = 0
    while n:
        digit = n % 10
        if digit == 0 or digit == 5:
            count += 1
        n = int(n / 10)
    return count
