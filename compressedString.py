
#6 return compressed string   
def compressedString(string):
    if isUnique(string): #calling the isUnique function to check if content is unique
        return string
    result = {string[0]:1}
    final_result = []
    
    
    for i in range(1, len(string)):
        if string[i] in result and string[i] == string[i-1]:
                result[string[i]] = result[string[i]] + 1
        else:
            final_result.append(result)
            result = {string[i]: 1}
    
    final_result.append(result) #add the last character to list                
        
    
    summ = ""
    for item in final_result:
        for x in item:
            summ = summ + x + str(item[x]) 
    
    if len(summ) >= len(string):
        return string
    else:
        return summ

print(compressedString("aabbaaacccbbbbcc"))


# Have a dictionary with the first letter and initial count 1 of the given string. Now loop through the remaining characters in the given string. If the current character is same as the immediate previous character, add the count. If it is not, append the current dictionary to a final list, and then create a new dictionary with the new character and an initial count of 1. Do this till the end of the list, then add the last character to the final list.list

# Now loop through the lists of dictionary and then concatenate the key and value pairs. If the resulting string lenght is greater than or equal to the initail string lenght, return the original string, if not, return the compressed string.