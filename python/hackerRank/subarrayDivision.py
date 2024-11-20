# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Example



# Lily wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .

# Function Description

# Complete the birthday function in the editor below.

# birthday has the following parameter(s):

# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month
# Returns

# int: the number of ways the bar can be divided
# Input Format

# The first line contains an integer , the number of squares in the chocolate bar.
# The second line contains  space-separated integers , the numbers on the chocolate squares where .
# The third line contains two space-separated integers,  and , Ron's birth day and his birth month.


# First of all, who the hell cares.

# Second of all - what is being returned is a number (the number of possible slices), not the specific slices that fit the crieteria.

def birthday(s, d, m):
    result = 0
    start_position = 0
    for slice in s: 
        if sum(s[start_position:m+start_position]) == d:
            result += 1
        else:
            pass
        start_position += 1
    return result

# Initialize a result at zero as well as a start position at zero. Loop through all possible slices whose length matches the criteria above.