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
# import random package
from random import random

#intiialize variables
listOfValueIndicesBiggerThenSpecificValue = []
listOfRandomValues = [random() for i in range(20)]
randomValueToCompareTo = random()

listOfRandomValues = sorted(listOfRandomValues)


# go through elements of list using indices
for valueIndex in range(0,len(listOfRandomValues)):
    # if the value at current Index is bigger then the random Target value
    # add it (index) to the list of value indices bigger then target 
    if listOfRandomValues[valueIndex] > randomValueToCompareTo:
        listOfValueIndicesBiggerThenSpecificValue.append(valueIndex)
    
# printing
print("List of indices of values greater then the random Value: " + str(listOfValueIndicesBiggerThenSpecificValue))

print("Sorted list of random values: " + str(listOfRandomValues))
print("Random value to be greater of: " + str(randomValueToCompareTo))

# print first occurance of the same random number in list if valid
if randomValueToCompareTo in listOfRandomValues:
    print("Index of random value in list: " + str(listOfRandomValues.index(randomValueToCompareTo)))