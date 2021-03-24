# -*- coding: utf-8 -*-
"""
This program only works with an integer argument.
Created for CST1101 Spring 2021, Week#08 Class#15.
This example program demonstrates the while statement.

Created on Tue 23-Mar-2021.
@author: ProfessorPatrick.
"""

# You may want to add sound effects - 
# Remove the comment hash at the start of the import statement
# Remove the comment hash at the start of the winsound.Beep calls

# import winsound
def countdown(n=10):
    while n > 0:
        # winsound.Beep(440, 500)
        # winsound.Beep(500, 200)
        print(n)
        n = n-1
    print("Blastoff!")
