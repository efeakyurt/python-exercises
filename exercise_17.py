# Write an algorithm that takes a list of integers and returns a new list where each number is doubled, 
# but only if the original number is even. Odd numbers should remain unchanged.

def doubledList(values):
    newList = []

    for number in values:
        if number % 2 == 0:
            number = number * 2
            newList.append(number)
        else:
            newList.append(number)

    return newList



mylist=[2,4,3,6,5,7]

print(doubledList(mylist))