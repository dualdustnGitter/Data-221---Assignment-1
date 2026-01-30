### Question 1
# Make program that mult's consec ints from 1 to product becomes greater then threshold
# 
#   store threshold
#   track current multiplier
#   print final product
###
print("Question 1:")

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
print()


### Question 2
# make a function that takes in a string that
# 
#   stores each word in a a dictionary as a key 
#   then the value is a list that lists 
###
print("Question 2:")

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
print()


### Question 3 
# Make function that that computes x^y
# given a list of pairs [x,y]
# break the x and y out by a for loop before running the function
# 
#   use for loop to unpack list pair
#   skip pairs where y is negative
#   store valid results and prints as list
###
print("Question 3:")

# initialiizing variables
# list of base and exponent number pairs
# empty list of answers of above list
listOfPairs = [[5,2], [3,-1], [4,3], [2,0]]
listOfPowerAnswers = []

# fucntion that computes and returns the exponent of 2 given numbers
def exponentPairs(baseNumber, exponentNumber) :
    return baseNumber ** exponentNumber

# loop through pair list in given base exponent pairs
for numberPairInList in listOfPairs:
    # get the base and exponent numbers
    baseNumber = numberPairInList[0]
    exponentNumber = numberPairInList[1]
    
    # checks if exponent is non negative
    # then calls the function and adds it to end of list of answers
    if exponentNumber >= 0:
        listOfPowerAnswers.append(exponentPairs(baseNumber,exponentNumber))


# print it
print(listOfPowerAnswers)
print()



### Question 4
# given list of random numbers 0-1
# and a another random value 0-1
#   
#   program that prints list of numbers's indices greater it
#   sorted list
#   value of the random chosen value
#   and first index of matching number (if any)
# 
### 
print("Question 4:")

from random import random

listOfValueIndicesBiggerThenSpecificValue = []
listOfRandomValues = [random() for i in range(20)]
randomValueToCompareTo = random()

listOfRandomValues = sorted(listOfRandomValues)



for valueIndex in range(0,len(listOfRandomValues)):
    if listOfRandomValues[valueIndex] > randomValueToCompareTo:
        listOfValueIndicesBiggerThenSpecificValue.append(valueIndex)
    
print("List of indices of values greater then the random Value: " + str(listOfValueIndicesBiggerThenSpecificValue))

print("Sorted list of random values: " + str(listOfRandomValues))
print("Random value to be greater of: " + str(randomValueToCompareTo))
if randomValueToCompareTo in listOfRandomValues:
    print("Index of random value in list: " + str(listOfRandomValues.index(randomValueToCompareTo)))
print()


### Question 5
# make a function that
# 
#   takes in 2 radii of 2 circles
#   area of circle
#   percentage of area covered of large circle by smaller circle (small area/big area)
### 
print("Question 5:")

# import math 
import math

# function that returns percentage covered 
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # if either radii are not greater then 0
    # return "invalid" response
    if areaOfCircle1 <= 0 or areaOfCircle2 <= 0:
            return "Invalid radii entered\nInputs must be greater then 0"

    # calculate two circle's areas
    areaOfCircle1 = radiusOfCircle1**2 * math.pi
    areaOfCircle2 = radiusOfCircle2**2 * math.pi

    # then calculate percentage of smaller circle covering the bigger circle
    # if first circle is bigger calculate circle1/circle2
    # otherwise calculate the other one
    if (areaOfCircle1 > areaOfCircle2):
        return str(areaOfCircle2/areaOfCircle1 * 100) + "%"
    return str(areaOfCircle1/areaOfCircle2 * 100) + "%"

print(circleAreaCoverage(1,2))



### Question 6
# make a function that takes in a list of numbers and returns a dictionary
#   
#   keys in dictionary are unique alues in the inputted list
#   values are percentage of numbers of values that are less than or equal to that key
###    

