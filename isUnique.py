#1 check if all characters in a string is unique
def isUnique(string):
    length = len(string)
    for i in range(length):
        for x in range(i+1, length):
            if string[i] == string[x]:
                return False
    return True      
        
print(isUnique("apple"))