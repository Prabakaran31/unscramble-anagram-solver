
# clean and final code of method 1

# to remove blank spaces in dictionary
def removeFromList(thelist, val):
    return [value for value in thelist if value != val]


# opens dictionary and reads it
def GetDic():
    try:
        dicopen = open("combo.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        print(f'Length of diclist is {len(diclist)}')
        diclist = removeFromList(diclist, '')
        print(f'Length of diclist is {len(diclist)}')

        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return


# to get the word and to get a non-repetitive list of letters in the given word
# it returns given word as list and the above-mentioned list
def getquery():
    query = input('enter the scrambled letters:')
    query = query.lower()
    allowed = 'qwertyuiopasdfghjklzxcvbnm'
    allowed = list(allowed)
    newQ = []
    for letter in query:
        for x in allowed:
            if letter == x:
                newQ.append(letter)
                pass
    p = list(newQ)
    grrh = [x for x in allowed if x not in p]
    return p, grrh


# removes longer and shorter words from dictionary
def listofwords(givenL):
    word = []
    for x in dic:
        if len(x) == givenL:
            word.append(x)
    '''print(f'the list of {givenL} lettered words are {word}' )'''
    return word



dic = GetDic()
p, grrh = getquery()
length = len(p)
final = listofwords(len(p))


# to find words that start with one of the letters in given word
def refineDict(dict, given, notp):

    brandnew = []

    for entry in dict:
        flag = 0
        dict1 = list(entry)
            # compare the dict1[i] with all letters in notp
            # if it matches with any one letter in notp pop the whole word from new
        for y in notp:
            for i in range(0, len(given)):
                if dict1[i] == y:
                    flag = flag + 1
        if flag == 0:
            brandnew.append(entry)

    return brandnew

refined = refineDict(final, p, grrh)


def checking(words, letters):

    cleared = [*set(letters)]
    #print(cleared)
    check = cleared
    #print(f'len(check) = {len(check)}')
    answer = []
    #print(f'cleared is {cleared}')

    for phrase in words:
        #print(phrase)
        for i in range(0,len(check)):
            check[i] = 0
        term = list(phrase)
        for w in term:
            #print(w)
            for i in range(0, len(check)):
                #print(f'cleared{[i]} is {cleared[i]}')
                cleared = [*set(letters)]

                if cleared[i] == w:
                    check[i] += 1
        flag = 0
        for x in check:
            if x != 0:
                flag += 1
        #print(phrase, flag)
        if flag == len(cleared):
            answer.append(phrase)
    return answer

anslist = checking(refined, p)
print(anslist)