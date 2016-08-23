__author__ = 'Jarod Jett'
# Write a function named right_justify that takes a string named s as a parameter and prints the
# string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    print(" "*(70 - len(s)), s) # Print 70 - the length of the string blank spaces, then print the string.
                                # Remember multiplying a print command repeats the character or string or whatever

right_justify("Hello World")