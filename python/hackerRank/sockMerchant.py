# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.

def sockMerchant(n, ar):
    # sort ar
    # initialize total and start position variables at zero
    
    # loop through the sorted ar and see if the current element is equal to the next. If so, increment total by 1 and start position by 2. If not, increment the start position by just 1 and try again.
    
    in_order = sorted(ar)
    total = 0
    start_position = 0
    
    while start_position < len(in_order) - 1:
        if in_order[start_position] == in_order[start_position + 1]:
            total += 1
            start_position += 2
        else:
            start_position += 1
    return total

