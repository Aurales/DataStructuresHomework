##Kyle Munoz
#Creating a Linear and Binary Search Function
import wordlist
import time

def LinearSearch(LookFor):
    word = wordlist.words
    wordindex = 0
    for i in word:
        if LookFor == i:
            return i
        wordindex +=1


#######Doesn't Work for proper Recursion
##def BinarySearchOutline(aword):
##    word = wordlist.words
##    LookFor = str(input("What word would you like to find?"))
##    wordindex = 0
##    for i in word:
##        if i == LookFor:
##            print(LookFor, wordindex)
##        elif i < word[(len(word)/2)]:
##            BinarySearch()
##def BinarySearch(aword, wordlist):
##    if word == wordlist[(len(wordlist)//2)]:
##        print(word, wordindex)
##    elif word < wordlist[(len(wordlist)//2)]:
##        wordlist = wordlist[0,wordlist(len(wordlist)//2)]
##        BinarySearch(aword, wordlist)
##    elif word > wordlist[(len(wordlist)//2)]:
##        wordlist = wordlist[wordlist(len(wordlist)//2),len(wordlist)]
##        BinarySearch(awrod, wordlist)
def BinarySearch(lowword, highword, word):

    middleword = ((lowword + highword) // 2)

    if word == wordlist.words[middleword]:
        return middleword

    elif int(lowword) == int(highword):
        if wordlist.words[lowword] == word:
            return lowword
        else:
            return  None
    else:
        if word < wordlist.words[middleword]:
            middleword = middleword - 1
            return BinarySearch(lowword, middleword, word)

        elif word > wordlist.words[middleword]:
            middleword = middleword + 1
            return BinarySearch(middleword, highword, word)



def TimeCheck():
    SearchWord = input("Please enter a word to compare times for Binary and Linear Searches: ")
    StartTime = time.clock()
    LinearSearch(SearchWord)
    StopTime = time.clock()
    TotalTime = StopTime - StartTime
    print("It took", TotalTime, "to do a linear search for", SearchWord)
    StartTime = time.clock()
    BinarySearch(0, len(wordlist.words), SearchWord)
    StopTime = time.clock()
    TotalTime = StopTime - StartTime
    print("It took", TotalTime, " to do a binary search for", SearchWord)
TimeCheck()
