#5 check if one string is zero or one edit away from the original string
def isOneAway(str1, str2):
    for i in str2:
        for x in str1:
            if i == x:
                str1 = str1[:str1.index(x)] + str1[str1.index(x)+1:] #omit the identical character
                break
    if len(str1) <= 1:
        return True
    else:
        return False
    
print(isOneAway('pale','bale'))


# Remove all the letters in string 2 from string 1. If length of string one is less than or equal to 1, that means that only a single change had occured.