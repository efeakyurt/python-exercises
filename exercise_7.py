# Write an algorithm that takes a list of integers and returns a new list where each number is doubled, 
# but only if the original number is even. Odd numbers should remain unchanged.




def makeList(values):
    newList=[]
    for number in values:
        if number % 2 == 0:
            newList.append(number*2)
        else:
            newList.append(number)

    return newList


mylist = [2,4,1,5,6,7,12]
print(makeList(mylist))


