# Import the `random` module to use the `randint()` method
import random
# Import `re` module to use the `findall()` method
import re


def get_file_lines(filename):
    """
    Takes in the name of a file and returns the lines of the file in a list by using the `readlines()` method.
    
    Parameters:
    filename (string): the name (with path, if needed) of the text file that contains the poem 

    Returns:
    list: the poem as a list of strings, each string a line of the poem
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
    
    Parameters:
    lines_list (list): a list of strings from a poem

    Returns:
    string: the poem as a string with the lines in backwards order
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

    Parameters:
    lines_list (list): a list of strings from a poem

    Returns:
    string: the poem as a string with the lines in random order
    """
    # Define a new string variable to hold all of the lines in one string
    random_poem = ""

    # Assign the length of the reversed list to a variable for easy access
    list_length = len(lines_list)

    # Iterate through the reversed list
    for i in range(list_length):
        # Add a line number and a random line to the output string by calling an element with a random index
        random_poem += f"{i + 1} {lines_list[random.randint(0, list_length - 1)]}"

    return random_poem


# Stretch Challenge #4
def lines_printed_custom(lines_list):
    """
    Takes in a list of lines of a file and returns the words on each line in random order 
    using the `randint()` method from the `random` library.
    
    Parameters:
    lines_list (list): a list of strings from a poem

    Returns:
    string: the poem as a string with the words in each line in random order
    """
    # Define a new string variable to hold all of the lines in one string
    custom_poem = ""

    # Assign the length of the reversed list to a variable for easy access
    list_length = len(lines_list)

    # Iterate through the list of lines
    for i in range(list_length):
        # Create new list variable for each line with each word in the line as an element in the list
        # Use `findall()` method to save each word from a string to a list without punctuation
        line_words = re.findall(r'\w+', lines_list[i])
        # Assign the length of the list of words in each line to a variable
        word_count = len(line_words)
        # Assign each line to an empty string so that it can be repopulated with its words in random order
        lines_list[i] = ""
        # Iterate through each line (which is a list of words)
        for j in range(word_count):
            # Add a random word in lower case from the list of words to its respective line with the line number
            lines_list[i] += line_words[random.randint(0, word_count - 1)].lower() + " "
        custom_poem += f"{i + 1} {lines_list[i]}\n"

    return custom_poem


# Stretch Challenge #1: write poems to a file
def write_to_file(poem):
    """
    Takes in a poem as a string and appends it to a file.
    
    Parameters:
    poem (string): a poem as a single string

    Returns:
    file: an output file with the poem appended to it
    """
    
    return poem
    
    


# Assign the list of lines from the poem to a new variable
poem_lines_list = get_file_lines("interstellar_poem.txt")
# print(poem_lines_list + "\n\n")
# print(lines_printed_backwards(poem_lines_list) + "\n\n")
# print(lines_printed_random(poem_lines_list) + "\n\n")
print(lines_printed_custom(poem_lines_list))