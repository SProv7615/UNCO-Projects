#Stephen Provost's Attempt#

dictionaryList = []
characterList = []
condensedDictionaryList = []
anagramList = []
wordfoundList = []
spellingbeeList = []
spellingbeewordsfoundlist = []
listofEight = []
bingoList = []

def call_from_n(num):
    n = 0
    while num > 0:
        n += num
        num-=1
    print(n)


def read_file_to_list(fileName):
    fileReader = open(fileName, "r")
    for lineRead in fileReader:
        dictionaryList.append(lineRead.strip('\n'))


def compare_To_List(wordToCompare):
    if wordToCompare in dictionaryList:
        print("True")


def create_list_of_characters(characters, listtostore):
    list(characters)
    for c in characters:
        listtostore.append(c)


def check_if_possible(givenWord,listtoplacewords):
    foundCharacters = ""
    foundCharacterLocations = []
    character_found = False
    for i in range(len(givenWord)):
        for j in range(len(characterList)):
            if givenWord[i] == characterList[j] and character_found == False and j not in foundCharacterLocations:
                character_found = True
                foundCharacters = foundCharacters + characterList[j]
                foundCharacterLocations.append(j)
            elif givenWord[i] != characterList[j] and j == len(characterList)-1 and character_found == False:
                foundCharacters = ""
                foundCharacterLocations.clear()
                return False
        character_found = False
    if foundCharacters == givenWord:
        listtoplacewords.append(givenWord)
        return True

def check_word_combos():
    for x in dictionaryList:
        if len(x) == len(characterList):
            condensedDictionaryList.append(x)
    for w in condensedDictionaryList:
        check_if_possible(w,anagramList)
    print(anagramList)


def spelling_bee_combos(t, rt):
    for x in dictionaryList:
        if len(x) >= 5:
            spellingbeeList.append(x)
    tilesList = list(t+rt)
    for w in spellingbeeList:
        if rt in w:
            check_if_possible_without_limits(w, tilesList, spellingbeewordsfoundlist)
    print(spellingbeewordsfoundlist)


def check_if_possible_without_limits(givenWord, listofLetters, listtoplacewords):
    foundCharacters = ""
    for w in range(len(givenWord)):
        for j in range(len(listofLetters)):
            if givenWord[w] == listofLetters[j]:
                foundCharacters = foundCharacters + listofLetters[j]
        if foundCharacters == givenWord:
            listtoplacewords.append(givenWord)


def bingo():
    bingocountlocations = []
    i = 0
    b = 0
    for x in dictionaryList:
        if len(x) == 8:
            listofEight.append(x)
    print(len(listofEight))
    while i < len(listofEight):
        while b < len(listofEight):
            if b == 0:
                bingoList.append(listofEight[i])
                bingocountlocations.append(1)
            else:
                characterList.clear()
                create_list_of_characters(listofEight[b],characterList)
                if check_if_possible(listofEight[i], bingoList):
                    listofEight.pop(b)
                    bingocountlocations.append(bingocountlocations.pop()+1)
            b = b + 1
        i = i + 1
        b = 0


call_from_n(15)
read_file_to_list("words.txt")
compare_To_List("zymurgy")
create_list_of_characters("ertiasn", characterList)
check_if_possible("zymurgy",wordfoundList)
check_word_combos()
spelling_bee_combos("rnabci", "l")
bingo()


#####################################################################
#                                                                   #
#               Number 1                                            #
#####################################################################

def Sumintegers(n):
    suma = 0
    while n != 0:
        suma = suma + n
        n = n - 1
    return suma


def count1(n):
    number = 0
    for a in range(n + 1):
        number += a
    return number


#####################################################################
#               Number 2                                            #
#                                                                   #
#####################################################################

def Checkword(w):
    wordlist = [line.strip() for line in open("words.txt")]
    lines = []
    for line in wordlist:
        lines.append(line.rstrip())
    if w in lines:
        return ("Valid")
    else:
        return ("Invalid")


#####################################################################
#               Number 3                                            #
#####################################################################

def Tiles(w, t):
    word = list(t)
    tiles = list(w)
    i = 0
    for x in tiles:
        for t in word:
            if x == t:
                word.remove(x)
                tiles.remove(t)
    if len(word) > 1:
        return ("False")
    else:
        return ("True")


#####################################################################
#               Number 4                                            #
#####################################################################


file = open('words.txt', 'r')
words = file.readlines()
file.close()
tiles = ["r", "e", "t", "a", "i", "n"]


def combinations(target, data):
    for tile in data:
        new_target = target.copy()
        new_data = data.copy()
        print(new_target)
        word = ""
        for letter in new_target:
            word = word + letter
        if word in words:
            print("Valid: " + word)
        combinations(new_target,
                     new_data)
    target = []
    list1 = []
    list2 = ["a", "b", "c"]
    combinations(target, tiles)




########################################
# Name: Devin K. Panikkar              #
# Instructor: Dr. Miller               #
# Assignment: Fun with Algorithms      #
# Date: 1/16/20                        #
########################################
print ("Assignment 1. Fun with algorithms!")
import time
import itertools
import string
import random
import string
import copy
#######################
# Problem 1           #
#######################
def PosIntSum(num):
    n = int(num)
    k =  1
    f = 0
    if(n>=1):
        for i in range (n):
            f += k
            k +=1
        if(n<1):
            f = "The number you entered is not a posotive integer. Try again"
        return f
def count1(n):
    num = 0
    for a in range(n+1):
        num += a
    return num

#######################
# Problem 2           #
#######################
def checker(word):
    file = open("words.txt")
    strings = file.read()
    #print(strings)
    search_word = word
    if search_word in strings:
        print(search_word, "is a valid word")
    else:
        print(search_word, "is not a valid word")

#######################
# Problem 3           #
#######################
def tiles(letterList, word):
    lowercasingList = ("".join(letterList)).lower()
    theList = list(lowercasingList)
    theWord = list(word.lower())

    possible = False
    if (len(theList) >= len(theWord)):
        for i in range (len(theWord)):
            if theWord[i] in theList:
                theList.remove(theWord[i])
                possible = True
            else:
                 possible = False
                 return possible
                 break
            return possible

#######################
# Problem 4           #
#######################

def WordUnscramble(letterList):
    lowercasingList = ("".join(letterList)).lower()
# permutations gives us all possible orderings
# that do not have repeated elements
    permList = list(itertools.permutations(lowercasingList))
    possWordList = []
    dictionaryfile = open("words.txt","r")
    wordDictionary = list(dictionaryfile.readlines())
# breaking words into lists of letters
    dictionaryWordLetters = [list(word.strip()) for word in wordDictionary]
# turning tuple into a list
    permList = [list(perm) for perm in permList]
# creating list of possible words
    for word in dictionaryWordLetters:
        for perm in permList:
            if (perm == word):
                possWordList.append("".join(word))
    if (possWordList == []):
        possWordList = "Sorry, no words were found using thoese letters."
    return possWordList
#######################
# Problem 5           #
#######################
def WordMaker(centerLetter,allLetters, minLetters, maxLetters):
    lowercasedList = list(("".join(allLetters)).lower())
    centerLetter = centerLetter.lower()
    letterCombin = []
    possWordList = []
    dictionaryfile = open("words.txt","r")
    wordDictionary = list(dictionaryfile.readlines())
    dictionaryWordLetters = [list(word.strip()) for word in wordDictionary]
    for i in range (minLetters,maxLetters+1):
        for combination in itertools.product(lowercasedList, repeat = i):
            letterCombin.append(list(combination))
    for word in dictionaryWordLetters:
        for combination in letterCombin:
            if combination == word:
                if centerLetter in word:
                    possWordList.append("".join(word))
    if possWordList == []:
        possWordList = "Sorry, no words were found with those letters."
    else:
        possWordList = ", ".join( repr(element) for element in possWordList)
    return possWordList
#######################
# Problem 6           #
#######################
def Bingo(wordLength):
    dictionaryfile = open("words.txt","r")
    wordDictionary = list(dictionaryfile.readlines())
    wordDictionary = [list(word.strip()) for word in wordDictionary]

    wordLengthList2 = []
    newCount2 = 1
    newBest2 = []
# This list below was created to keep track of the sets
# of letters that have already been accounted for
    newList2 = []
    for word in wordDictionary:
        if(len(word) == wordLength+1):
            word = sorted(word)
            wordLengthList2.append(word)
# The loop below counts the that sorted word. If the
# sorted word has already been added to the list, it will
# not be counted again.
    for i in range(len(wordLengthList2)):
        count = wordLengthList2.count(wordLengthList2[i])
        if wordLengthList2[i] not in newList2:
            newList2.append([wordLengthList2[i],count])
# Within the new additions to the list the set of letters
# with the greatest count(the number of words that can)
# be made is kept.
            if count > newCount2:
                newBest2 = [wordLengthList2[i], count]
                newCount2 = count
# If the counts are the the same both sets are kept along
# with their number of words that can be made.
            if count == newCount2:
                newBest12 = newBest2
                if newBest12 != [wordLengthList2[i],count]:
                    newBest2 = [newBest2,[wordLengthList2[i],count]]
                else:
                    newBest2 = newBest12
                newCount2 = count
    return newBest2


import itertools


# sum of the first n positive integers
def Sumintegers(n):
    # n Number
    suma = 0
    while n != 0:
        suma = suma + n
        n = n - 1
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
def CheckwordWtiles(t, w):
    # t tiles to use
    # w word to check
    titles = list(t)
    word = list(w)
    titles.sort()
    word.sort()
    while (len(titles) > 0 and len(word) > 0):
        if titles[0] == word[0]:
            titles.remove(titles[0])
            word.remove(word[0])
        else:
            titles.remove(titles[0])
    if len(word) >= 1:
        return False
    elif (len(word) == 0):
        return True


# see what words can be made with a given set of titles
# type titles with not spaces
def WordsWtitles(t):
    # t tiles
    valid = []
    with open("words.txt") as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    for y in lines:
        titles = list(t)
        word = list(y)
        titles.sort()
        word.sort()
        while (len(titles) > 0 and len(word) > 0):
            if titles[0] == word[0]:
                titles.remove(titles[0])
                word.remove(word[0])
            else:
                titles.remove(titles[0])
        if len(word) >= 1:
            r = 0
        elif (len(word) == 0):
            valid.append(y)
    return valid


# solve the New York Times's puzzle
# type letters with no spaces
def puzzle(t, c):
    ##t introduce all the letters
    ##c specify witch letter is in the center
    valid = []
    with open("words.txt") as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    for y in lines:
        titles = list(t * 7)
        word = list(y)
        titles.sort()
        word.sort()
        while (len(titles) > 0 and len(word) > 0):
            if titles[0] == word[0]:
                titles.remove(titles[0])
                word.remove(word[0])
            else:
                titles.remove(titles[0])
        if len(word) >= 1:
            r = 0
        elif (len(word) == 0 and len(y) >= 5 and c in y):
            valid.append(y)
    return valid


# see what set of titles makes the most words
# The problem with this methods is that it is too slow
# to see it works you can try it with smaller combinations like 3 or 4
def Bingo():
    maximun = 0
    bestcomb = ""
    dummylist = []
    letters = "qwertyuiopasdfghjklzxcvbnm"
    lista = list(letters)
    check = ""
    with open("words.txt") as f:
        lines = []
        for line in f:
            if len(line.strip()) == 8:  # change number here
                lines.append(line.strip())
    for combination in itertools.combinations(lista, 8):  # change number here
        dummylist = []
        check = ""
        for a in combination:
            check = check + a
        for y in lines:
            word = list(y)
            titles = list(check)
            titles.sort()
            word.sort()
            while (len(titles) > 0 and len(word) > 0):
                if titles[0] == word[0]:
                    titles.remove(titles[0])
                    word.remove(word[0])
                else:
                    titles.remove(titles[0])
            if len(word) >= 1:
                r = 0
            elif (len(word) == 0):
                dummylist.append(y)
        if len(dummylist) >= maximun:
            maximun = len(dummylist)
            bestcomb = str(combination) + "# words " + str(maximun)
    return bestcomb