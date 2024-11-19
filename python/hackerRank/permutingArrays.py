# There are two -element arrays of integers,  and . Permute them into some  and  such that the relation  holds for all  where .

# There will be  queries consisting of , , and . For each query, return YES if some permutation ,  satisfying the relation exists. Otherwise, return NO.

# Example



# A valid  is  and :  and . Return YES.

# Function Description

# Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

# twoArrays has the following parameter(s):

# int k: an integer
# int A[n]: an array of integers
# int B[n]: an array of integers
# Returns
# - string: either YES or NO

# Input Format

# The first line contains an integer , the number of queries.

# The next  sets of  lines are as follows:

# The first line contains two space-separated integers  and , the size of both arrays  and , and the relation variable.
# The second line contains  space-separated integers .
# The third line contains  space-separated integers .
# Constraints

# Sample Input

# STDIN       Function
# -----       --------
# 2           q = 2
# 3 10        A[] and B[] size n = 3, k = 10
# 2 1 3       A = [2, 1, 3]
# 7 8 9       B = [7, 8, 9]
# 4 5         A[] and B[] size n = 4, k = 5
# 1 2 2 1     A = [1, 2, 2, 1]
# 3 3 3 4     B = [3, 3, 3, 4]
# Sample Output

# YES
# NO
# Explanation

# There are two queries:

# Permute these into  and  so that the following statements are true:

# , , and . To permute  and  into a valid  and , there must be at least three numbers in  that are greater than .


# Fastest way to do this is to sort one array in ascending and the other in descending order, so that the smallest values in one are paired with / "helped" by the largest in the other. Will help identify failures of the condition above in less time.

def twoArrays(k, A, B):
    #start with sorting A ascending and B descending.
    # loop through the range of n, adding A[n] and B[n] and seeing if any combo satisfies the condition of being >= k.
    sorted_A = sorted(A)
    sorted_B = sorted(B, reverse=True)
    
    for n in range(len(A)):
        if sorted_A[n] + sorted_B[n] < k:
            return "NO"
    
    return "YES"

#returning YES outside of the loop ensures that all combinations run. If any of them satisfy the condition to return NO then the loop ends and that's that. But, if every combination isn't less than k then the loop ends and we get a YES.