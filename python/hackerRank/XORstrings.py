# lmao so this one in hackerRank asks you to debug code that doesn't exist, soooo I guess we are writing from scratch! 

def strings_xor(s1, s2):
    result = ""
    
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += "0"
        else:
            result += "1"
    return result
    
s1 = input().strip()
s2 = input().strip()

print(strings_xor(s1,s2))