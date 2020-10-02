Make School CS 1.0 

Project: Poetry Slam

This project uses Python 3.7.4.

The purpose of this project is to rearrange the content of a poem to potentially find new creative interpretations. I chose the poem "Do no go gentle into that good night", because it was featured in the movie "Interstellar". The poem is saved in a text file that is in the same directory as the Python file that contains the code. 

When the program is run, the user is introduced to the purpose of the program and is presented with a menu of options. The first prompt asks which function the user would like to use, and the second prompt asks how the user would like the output to be presented. The Python file includes four functions for rearranging the poem. The first function, `get_file_lines(filename)`, takes in a file name as a string and returns a list of strings, with each line of the input poem as an element. This first function is used to provide the input for the other three functions, all of which take in a list of strings as an input parameter. The second function, `lines_printed_backwards(lines_list)`, returns a string with the poem in reverse order. Each line is preserved in its original order from left to right, but the order of the strings is reversed. The original line number is also printed to the left of each line, so the output is lines 24 through 1 from top to bottom. The third function, `lines_printed_random(lines_list)`, returns the lines in random order. There are still 24 lines, but the order is random and there might also be some repeats. The fourth function, `lines_printed_custom(lines_list)`, returns the poem with all 24 lines in the same order, but the word order in each line is randomized. The punctuation and capitalization within each line was also removed to increase the likelihood of producing more cogent lines. The words in each line might also be repeated, like the full lines in the third function, because this function uses the same `randint()` method to access random elements in a list.

The output can either be printed to the console or written to a file called output.txt. 
