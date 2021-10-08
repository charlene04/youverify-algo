#2 check if one string is permutaion of the other   
def isPermutation(str1, str2):
    l1, l2 = len(str1), len(str2)
    if l1 != l2:
        return False
    for i in str1:
        for x in str2:
            if i == x:
                str2 = str2[:str2.index(x)] + str2[str2.index(x)+1:] #omit the identical character
                break
    if len(str2) == 0:
        return True
    else:
        return False
print(isPermutation("magnet", "tnemga")) 