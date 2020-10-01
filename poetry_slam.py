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


def lines_printed_backwards(lines_list):
    """
    Takes in a list of lines of a file and returns the lines in backwards order 
    with original line numbers in front of each line.
    Input: a list of string
    Output: a string
    """
    # Reverse the order of the input list
    lines_list.reverse()
    # Define a new string variable to hold all of the lines in one string
    backwards_poem = ""
    # Assign the length of the reversed list to a variable for easy access
    list_length = len(lines_list)
    # Iterate through the reversed list
    for i in range(list_length):
        # Add the line number and the line to the output string
        backwards_poem += f"{list_length - i} {lines_list[i]}"
    return backwards_poem


def lines_printed_random(lines_list):
    """
    Takes in a list of lines of a file and returns the lines in random order 
    using the `randint()` method from the `random` library.
    Input: a list of strings
    Output: a string
    """
    # Define a new string variable to hold all of the lines in one string
    backwards_poem = ""
    # Assign the length of the reversed list to a variable for easy access
    list_length = len(lines_list)
    # Iterate through the reversed list
    for i in range(list_length):
        # Assign `i` to another variable to avoid an IndexError upon adding 1 in the f-string
        line_counter = i
        # Add a line number and a random line to the output string by calling an element with a random index
        backwards_poem += f"{line_counter + 1} {lines_list[random.randint(0, list_length)]}"
    return backwards_poem


# Stretch Challenge #4
def lines_printed_custom(lines_list):
    """
    Takes in a list of lines of a file and returns the words on each line in random order 
    using the `randint()` method from the `random` library.
    Input: a list of strings
    Output: a string
    """
    # Define a new string variable to hold all of the lines in one string
    backwards_poem = ""
    # Assign the length of the reversed list to a variable for easy access
    list_length = len(lines_list)
    # Iterate through the reversed list
    for i in range(list_length):
        # Assign `i` to another variable to avoid an IndexError upon adding 1 in the f-string
        line_counter = i
        # Add a line number and a random line to the output string by calling an element with a random index
        backwards_poem += f"{line_counter + 1} {lines_list[random.randint(0, list_length)]}"
    return backwards_poem


# Assign the list of lines from the poem to a new variable
poem_lines_list = get_file_lines("interstellar_poem.txt")
# print(poem_lines_list)
# print(lines_printed_backwards(poem_lines_list))
print(lines_printed_random(poem_lines_list))