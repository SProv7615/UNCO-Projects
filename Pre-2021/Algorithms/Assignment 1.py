import itertools

# sum of the first n positive integers
def Sumintegers(n):
    #n Number
    suma=0
    while n != 0:
        suma=suma + n
        n=n-1
    return suma

# check if it is a valid word to play
def Checkword(w):
    # w word
    with open("words.txt") as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    if w in lines:
        return "valid word"
    else:
        return "invalid word"

# check word with a given set of titles
# type titles with not spaces
def CheckwordWtiles (t , w ):
    #t tiles to use
    #w word to check
    titles = list(t)
    word = list(w)
    titles.sort()
    word.sort()
    while(len(titles)>0 and len(word)>0):
        if titles[0]==word[0]:
            titles.remove(titles[0])
            word.remove(word[0])
        else:
            titles.remove(titles[0])
    if len(word) >= 1:
        return False
    elif(len(word)==0):
        return True

# see what words can be made with a given set of titles
# type titles with not spaces
def WordsWtitles(t):
    #t tiles
    valid =[]
    with open("words.txt") as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    for y in lines:
        titles = list(t)
        word = list(y)
        titles.sort()
        word.sort()
        while(len(titles)>0 and len(word)>0):
            if titles[0]==word[0]:
                titles.remove(titles[0])
                word.remove(word[0])
            else:
                titles.remove(titles[0])
        if len(word) >= 1:
            r=0
        elif(len(word)==0):
            valid.append(y)
    return valid          

# solve the New York Times's puzzle
# type letters with no spaces
def puzzle(t, c):
    ##t introduce all the letters
    ##c specify witch letter is in the center
    valid =[]
    with open("words.txt") as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    for y in lines:
        titles = list(t*7)
        word = list(y)
        titles.sort()
        word.sort()
        while(len(titles)>0 and len(word)>0):
            if titles[0]==word[0]:
                titles.remove(titles[0])
                word.remove(word[0])
            else:
                titles.remove(titles[0])
        if len(word) >= 1:
            r=0
        elif(len(word)==0 and len(y) >= 5 and c in y):
            valid.append(y)
    return valid

# see what set of titles makes the most words
# The problem with this methods is that it is too slow
# to see it works you can try it with smaller combinations like 3 or 4
def Bingo():
    maximun = 0
    bestcomb = ""
    dummylist =[]
    letters ="qwertyuiopasdfghjklzxcvbnm"
    lista = list(letters)
    check =""
    with open("words.txt") as f:
            lines = []
            for line in f:
                if len(line.strip()) == 8: # change number here
                    lines.append(line.strip())
    for combination in itertools.combinations(lista, 8): # change number here
        dummylist =[]
        check=""
        for a in combination:
            check= check+ a
        for y in lines:
            word = list(y)
            titles =list(check)
            titles.sort()
            word.sort()
            while(len(titles)>0 and len(word)>0):
                if titles[0]==word[0]:
                    titles.remove(titles[0])
                    word.remove(word[0])
                else:
                    titles.remove(titles[0])
            if len(word) >= 1:
                r=0
            elif(len(word)==0):
                dummylist.append(y)
        if len(dummylist) >= maximun:
            maximun = len(dummylist)
            bestcomb =  str(combination) + "# words " + str(maximun)
    return bestcomb
     

        
    
        
    
    
        
        
