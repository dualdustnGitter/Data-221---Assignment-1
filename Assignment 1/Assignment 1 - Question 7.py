### Question 7
# create a function that converts seconds (since midnight) into
#   
#   Hours
#   Minutes
#   Seconds 
#   AM/PM
###  
print("Question 7:")

def convertSecondsToExpanded(secondsInput):
    # checks if time inputted is valid (between 0 seconds and 24 hours)
    # if invalid return amazing invalid message
    if (secondsInput < 0):
        return("Invalid time entered: Time inputted is less then 0 seconds")
    elif(secondsInput > 86400):
        return("Invalid tiem entered: Tiem inputted is more then 86400 seconds (24 hours)")
    
    # Set period as AM first
    periodElement = "AM"

    # create other variables, initial hours, minutes and seconds
    hoursElement = secondsInput // 3600
    actualHoursElement = hoursElement

    minutesElement = secondsInput // 60 - hoursElement*60

    actualSecondsElement = secondsInput - hoursElement*3600 - minutesElement*60

    # convert hours to 12 hour format
    # also make sure to change period to PM if 12 (noon) is reached/passed
    if hoursElement >= 12:
        periodElement = "PM"
        if hoursElement > 12:
            actualHoursElement = hoursElement - 12


    # return output
    return ("Current time:\n\tHours: " + str(actualHoursElement) 
            + "\n\tMinutes: " + str(minutesElement)
            + "\n\tSeconds: " + str(actualSecondsElement)
            + "\n\tPeriod: " + periodElement)

print(convertSecondsToExpanded(45030))