# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

# Example

# The string contains all letters in the English alphabet, so return pangram.

# Function Description

# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

# pangrams has the following parameter(s):

# string s: a string to test
# Returns

# string: either pangram or not pangram
# Input Format

# A single line with string .

# Constraints


# Each character of , 

# Sample Input

# Sample Input 0

# We promptly judged antique ivory buckles for the next prize

# Sample Output 0

# pangram

# Sample Explanation 0

# All of the letters of the alphabet are present in the string.

# Sample Input 1

# We promptly judged antique ivory buckles for the prize

# Sample Output 1

# not pangram

# Sample Explanation 0

# The string lacks an x.


def pangrams(s):
    alphabet = list(string.ascii_lowercase)
    test = [letter for letter in set(s.lower()) if letter != " "]
    
    if len(alphabet) == len(test):
        return "pangram"
    else:
        return "not pangram"

# list comps look really slick don't they. need to import string at the top of the file to utilize string.ascii_lowercase. this creates a list of all of the letters in the alphabet