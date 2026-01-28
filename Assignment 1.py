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

def dictionaryTheString(stringInput):
    lastIndexNumber = 0
    currentIndexNumber = 0
    dictionaryOfWordsInString = {}

    for characterInStringInput in stringInput:
        if characterInStringInput == " ":
            dictionaryTheString[lastIndexNumber, currentIndexNumber] = "length: " + ""
        currentIndexNumber = currentIndexNumber + 1
