# Write an algorithm that takes a list of integers and returns a 
# new list containing only the positive numbers from the original list.

def createList(values):
    newList = []

    for number in values:
        if number > 0 :
            newList.append(number)

    return newList


mylst=(-8,5,3.5,-6.5,-7,11)
print(createList(mylst))