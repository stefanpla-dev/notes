# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6, and 9. The sum is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def sumBelow(num):
    multiples3 = sum(i for i in range(num) if i%3 == 0)
    multiples5 = sum(i for i in range(num) if i%5 == 0)
    multiples15 = sum(i for i in range(num) if i%15 == 0)

    return multiples3+multiples5-multiples15


def sumBelowTheRemix(num):
    return sum(i for i in range(num) if i%3==0 or i%5==0)


# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
# The order of the sequence has to stay the same.

def distinct(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]