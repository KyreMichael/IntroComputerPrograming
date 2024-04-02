#
# Kyre M Shamwell
# Comp 163-001
# May 5 2022
# In this program I will be using a passage or sentence coming from user input to display the amount of vowels, words, a vowel count, and weither y is seen as a vowel or not using recursion. 
#

# In this function I will be using my recursive function to check and see how many vowels are in my passage/sentence and retuning it back to the function vowels
def vowels(sentenceVowels):
    sentenceVowels = sentenceVowels.lower()
    if not sentenceVowels:
        return 0
    elif sentenceVowels[0] in ("a", "e", "i", "o", "u"):
        return 1 + vowels(sentenceVowels[1:])
    else:
        return vowels(sentenceVowels[1:])

# This recursive function counts each words in the passage by catching each word before a space and returning the list back to the function       
def countingWords(thesentence, theSplit=' '):
    if not thesentence:
        return 0
    return [thesentence[:thesentence.index(theSplit)]] + countingWords(thesentence[thesentence.index(theSplit)+1:]) if theSplit in thesentence else [thesentence]  

# For the next 6 functions I look for every single vowel in the passage one by one and print out how many specific vowel was in the passage or sentence 

# Count for A    
def countVowelsA(vowelA):
    vowelA = vowelA.lower()
    if not vowelA:
        return 0
    elif vowelA[0] in ("a"):
        return 1 + countVowelsA(vowelA[1:])
    else:
        return countVowelsA(vowelA[1:])

# Count for E
def countVowelsE(vowelE):
    vowelE = vowelE.lower()
    if not vowelE:
        return 0
    elif vowelE[0] in ("e"):
        return 1 + countVowelsE(vowelE[1:])
    else:
        return countVowelsE(vowelE[1:])

# Count for I
def countVowelsI(vowelI):
    vowelI = vowelI.lower()
    if not vowelI:
        return 0
    elif vowelI[0] in ("i"):
        return 1 + countVowelsI(vowelI[1:])
    else:
        return countVowelsI(vowelI[1:])

# Count for O
def countVowelsO(vowelO):
    vowelO = vowelO.lower()
    if not vowelO:
        return 0
    elif vowelO[0] in ("o"):
        return 1 + countVowelsO(vowelO[1:])
    else:
        return countVowelsO(vowelO[1:])   
    
# Count for U
def countVowelsU(vowelU):
    vowelU = vowelU.lower()
    if not vowelU:
        return 0
    elif vowelU[0] in ("u"):
        return 1 + countVowelsU(vowelU[1:])
    else:
        return countVowelsU(vowelU[1:])   

# Count for Y rules
def imVowelY(vowelY):
    return vowelY.lower() in ['y']
def countVowelsY(findingY, y):
    vowels = ["a", "e", "i", "o", "u"]
    theVowelList = [char for char in findingY if char in vowels]
    # This is my for loop where I called for a lot of the Y rule things to get it either to print that Y isnt a vowel or count Y 
    for v in theVowelList:
        if v in vowels:
            return ("0 Since there are other vowels in the passage Y is not a vowel")
        elif findingY[-1] == "y":
            return ("Since Y is either followed by the last vowel or consonant: Y is a vowel") 
        elif findingY[-1] != "y":
            return ("0 Since Y is not either followed by the last vowel or consonant: Y is not a vowel")    
        else:
            return ("Since there are no other vowels Y is seen as a vowel") 
    if (y == 1):
        return imVowelY(findingY[y - 1])
    return (countVowelsY(findingY, y - 1) + imVowelY(findingY[y - 1]))

# Main sentence which is run through each function above
entersentence = input("Enter you own sentence/passage : ")

# Print statements for user
print("The amount of words in the sentence/passage are", len(countingWords(entersentence)))
print("The amount of vowels in the sentence/passage are", vowels(entersentence))
print("The amount of A's are", countVowelsA(entersentence))
print("The amount of E's are", countVowelsE(entersentence))
print("The amount of I's are", countVowelsI(entersentence))
print("The amount of O's are", countVowelsO(entersentence))
print("The amount of U's are", countVowelsU(entersentence))
print("The amount of Y's are", countVowelsY(entersentence, len(entersentence)))
