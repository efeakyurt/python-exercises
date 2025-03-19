# Write an algorithm that finds the maximum number in a list of integers

numberList = [1,4,6,2,9,3]

def findMax(numberList):
    if len(numberList) == 0:
        return False
    
    max_number = numberList[0] #initializing the counter 

    for number in numberList:
        if number > max_number:
            max_number = number

    return max_number


print(findMax(numberList))