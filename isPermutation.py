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


# Confirm that the length of the strings are equal first.
# Loop through both strings, where any character in string 1 matches a character in string 2, delete the character in string 2 and break the loop incase there are other matching characters too. 

# After the operation, if no character remains in string 2