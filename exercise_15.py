# Write an algorithm that takes a list of integers and returns the sum of all the odd numbers in the list.

def sumOdd(values):
    total = 0

    for number in values:
        if number % 2 == 1:
            print(number, "is odd")
            total += number
        
    return ("The total is", total)


mylist=(1,2,4,6,8,9)

print(sumOdd(mylist))