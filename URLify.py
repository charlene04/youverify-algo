#3 URLify a given string by replacing spaces with %20
def URLify(string):
    ls = []
    ln = len(string)
    while ' ' in string:
        for i in string:
            if i == ' ':
                ls.append(string[:string.index(i)])
                string = string[string.index(i)+1:] #cut characters up to the space and return the rest
    else:
        ls.append(string) #append the last word
        
    summ = ''
    for word in ls:
        if ls[-1] != word: #check if it is not the last word
            summ = summ + word + '%20'
        else:
            summ = summ + word
    return summ

print(URLify("Mr john Smith Aba"))


# Run a while loop to check if there is still space character in the given string. After that, run a for loop to get the index where the space char exists. Cut the characters up to the space character and add them to a list, then return the new string omitting the previously cut out one. Do this till there is no more space characters, then add the last word to the list.

# Finally, loop through the list, and concatenate with the %20