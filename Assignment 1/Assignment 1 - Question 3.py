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