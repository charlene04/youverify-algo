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