# -*- coding: utf-8 -*-
"""
This program only works with an integer argument.
Created for CST1101 Spring 2021, Week#08 Class#15.
This example program demonstrates counting digits.

Created on Tue 23-Mar-2021.
@author: ProfessorPatrick.
"""

# This function counts the number of digits in an integer 
# For trace function scaffolding remove # before each print()

def num_digits(n=710):
    count = 0
    # print("count", "\t", "n")
    # print("-----", "\t", "-")
    # print(n, "\t", count)
    while n:
        count += 1
        n = int(n / 10)
        # print(n, "\t\t", count)
    return count

# Trace the values of n and count for each state of execution
