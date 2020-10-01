# Import the `random` module for random rearrangements
import random

def get_file_lines(filename):
    """
    Takes in the name of a file and returns the lines of the file in a list by using the `readlines()` method.
    Input: a string
    Output: a list of strings
    """
    # Open the input file for reading and save it to `infile`
    infile = open(filename, "r")
    # Use the `readlines()` method to save each line to a list
    list_of_lines = infile.readlines()
    # Close the input file
    infile.close()
    return list_of_lines

