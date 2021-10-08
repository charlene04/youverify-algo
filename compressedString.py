
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