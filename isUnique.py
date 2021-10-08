#1 check if all characters in a string is unique
def isUnique(string):
    length = len(string)
    for i in range(length):
        for x in range(i+1, length):
            if string[i] == string[x]:
                return False
    return True      
        
print(isUnique("apple"))


# Get one letter, and loop through the remaining (to the right end) to see if there is any match. Do this for every letter.