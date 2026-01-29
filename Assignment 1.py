### Question 1
# Make program that mult's consec ints from 1 to product becomes greater then threshold
# 
#   store threshold
#   track current multiplier
#   print final product
###

def printMultiplyUptoThreshold(threshold):
    # track current product, and current Multiplier
    totalProduct = 1
    currentNumberMultiplier = 1

    # loop until product is bigger then the threshold
    while totalProduct <= threshold:
        # multiply current multiplier with previous product
        # then add one to the multiplier
        totalProduct = totalProduct * currentNumberMultiplier
        currentNumberMultiplier = currentNumberMultiplier + 1

    # subtract multiplier to actual current multiplier
    currentNumberMultiplier = currentNumberMultiplier - 1

    # show current Multiplier, and end product
    print("Current Multiplier: " + str(currentNumberMultiplier))
    print("Product reached: " + str(totalProduct))

# run the function (program)
printMultiplyUptoThreshold(100)


### Question 2
# make a function that takes in a string that
# 
#   stores each word in a a dictionary as a key 
#   then the value is a list that lists 
###

def dictionaryTheStringProperties(stringInput):
    # initial variable setting up
    parityOfWord = ""
    lastIndexNumber = 0
    currentIndexNumber = 0
    dictionaryOfWordsInString = {}

    # loop through all characters in String Input
    for characterInStringInput in stringInput:
        # if characters are seperated by space, its a word
        if characterInStringInput == " ":
            # make the word stored in its own variable
            wordChosenWithinInput = stringInput[lastIndexNumber:currentIndexNumber]

            # if its not the first word then remove the space at the start
            if (lastIndexNumber != 0):
                wordChosenWithinInput = stringInput[lastIndexNumber+1:currentIndexNumber]
        
            # determines length and parity of word
            lengthOfWordWithinInput = len(wordChosenWithinInput)
            parityOfWord = "odd"
            if (lengthOfWordWithinInput % 2 == 0):
                parityOfWord = "even"

            # add the word and its properties into the dictionary
            # and update last index where a space was found
            dictionaryOfWordsInString[wordChosenWithinInput] = {"length": lengthOfWordWithinInput, "parity": parityOfWord}
            lastIndexNumber = currentIndexNumber
        
        # update current index
        currentIndexNumber = currentIndexNumber + 1

    # deals with last word in String
    # get the word without the space
    # get the length and parity
    # then add to the dictionary
    wordChosenWithinInput = stringInput[lastIndexNumber+1:currentIndexNumber]
    lengthOfWordWithinInput = len(wordChosenWithinInput)
    parityOfWord = "odd"
    if (lengthOfWordWithinInput % 2 == 0):
        parityOfWord = "even"


    dictionaryOfWordsInString[wordChosenWithinInput] = {"length": lengthOfWordWithinInput, "parity": parityOfWord}

    return(dictionaryOfWordsInString)

print(dictionaryTheStringProperties("data science rules lol"))



### Question 3 
# Make function that that computes x^y
# given a list of pairs [x,y]
# 
#   use for loop to unpack list pair
#   skip pairs where y is negative
#   store valid results and prints as list
###