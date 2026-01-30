### Question 8
# create dataframe with provided column data
#   
#   after converting dictionary to DataFrame
#   add another column that's derived from existing columns (here ill just make the deriving be the sum)
###  
print("Question 8:")

# import pandas library ans assign it as "pd"
import pandas as pd

# take in data (dictionary) input 
data = {
    "A": [1,2,2,1],
    "B": [3.1,4.2,1.5,6.3],
    "C": [800,150,400,210]
}

# convert dictionary to DataFrame usign pandas
dataFrameConverted = pd.DataFrame(data)

# derive a new column "D" from summing up values in column "A", "B" and "C"
# then print it
dataFrameConverted["D"] = dataFrameConverted["A"] + dataFrameConverted["B"] + dataFrameConverted["C"]
print(dataFrameConverted)