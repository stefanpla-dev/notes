# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Constraints

# Output Format

# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output

# 15
# Explanation

# The primary diagonal is:

# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:

#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15

# Note: |x| is the absolute value of x

##########################

# len(arr) is a cheeky way to access the length (and height, in a way) of the input array
#initialize a sum for the primary/secondary diagonals at zero
#use a loop to iterate through all of the sublists
#return the absolute value of the difference between the two. 

def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - i - 1]

    return abs(primary_diagonal_sum - secondary_diagonal_sum)