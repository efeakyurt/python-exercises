# Write an algorithm that takes a list of integers and returns the sum of all the odd numbers in the list.

def sumOdd(value):
    total = 0
    for number in value:
        if number % 2 == 1:
            total += number 
    
    return total


my_odd = [1,3,4,2,7,11]
print(sumOdd(my_odd))