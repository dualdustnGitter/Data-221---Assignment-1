### Question 6
# make a function that takes in a list of numbers and returns a dictionary
#   
#   keys in dictionary are unique alues in the inputted list
#   values are percentage of numbers of values that are less than or equal to that key
###    
print("Question 6:")

def percentageOfElementsLesserEqual(listOfNumbers):
    # initializing variables
    sortedListofNumbers = sorted(listOfNumbers)
    dictionaryOfNumbersWithCount = {}
    dictionaryOfNumbersWithPercentages = {}

    # first make a dictionary of sorted list with keys being unique in list
    # the value of the keys are the amount of occurences in the list
    for numberInList in sortedListofNumbers:
        # if unique key alreayd in list then add 1
        # otherwise set it as 1 occurence
        if numberInList in list(dictionaryOfNumbersWithCount.keys()):
            dictionaryOfNumbersWithCount[numberInList] = dictionaryOfNumbersWithCount[numberInList] + 1
        else:
            dictionaryOfNumbersWithCount[numberInList] = 1


    # create a dictionary with the percentages of elements lesser then or equal to the current unique key
    for uniqueKey in list(dictionaryOfNumbersWithCount.keys()):
        # make variable of current index of current key
        # then add up the key number of elements before that value then divide by total of elements in list
        currentIndexOfUniqueKey = list(dictionaryOfNumbersWithCount.keys()).index(uniqueKey)
        percentageOfElements = (sum(list(dictionaryOfNumbersWithCount.values())[0:currentIndexOfUniqueKey+1])) / len(listOfNumbers)

        # set value of keys as the percentage
        dictionaryOfNumbersWithPercentages[uniqueKey] = str(percentageOfElements*100) + "%"


    return(dictionaryOfNumbersWithPercentages)

print(percentageOfElementsLesserEqual([3,1,2,3,4,2]))