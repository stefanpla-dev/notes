return 10 in [a,b,a+b]

^ this is a boolean statement, which will return True if 10 is either a, b or a+b. the "in" will check for 10's equality to any of the elements in the provided list. Membership operator.

sorted([a,b,c]) -> sorting in order, default is numeric. can add a key parameter inside () to change this default. Key can be a custom method defined inside the same class.

max(n1, n2, n3...) OR max(iterable)

sequence[start:stop:step] -> fancy slicing. if omitted, slicing starts from the beginning of the sequence. if stop is ommitted, slicing continues until the end of the sequence. Step determines how many elements to skip between each item. Default is one.