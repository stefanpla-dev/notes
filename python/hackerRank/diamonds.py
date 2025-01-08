def diamond(n):
    if n <= 0 or n%2 == 0:
        return None
    
    diamond_lines = []
    
    for i in range(1,n+1,2):
        spaces = (n-i) // 2
        diamond_lines.append(" "*spaces+"*"*i)
        
    for i in range(n-2,0,-2):
        spaces = (n-i)//2
        diamond_lines.append(" "*spaces+"*"*i)
        
    return "\n".join(diamond_lines)+"\n"

# So what you get in the end is something to the effect of 

#   *
#  ***
#   *

# if n = 3

#What I learned here is that you can use the range function in python to go in reverse. The range(n-2,0,-2) implies that the range can't go below zero, but that the "step" is -2.