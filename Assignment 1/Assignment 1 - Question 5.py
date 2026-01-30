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
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
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