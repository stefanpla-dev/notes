# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, 1)]

# fun list comp trick. enumerate handles the incremeneting of the number at the front of the format string so you don't have to do so manually.