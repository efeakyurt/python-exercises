# Write an algorithm that counts how many even numbers are in a given list of integers.


def evenNumbers(values):
    count = 0  #count is initially is zero 
    for number in values:
        if number % 2 == 0:
            count += 1
    return count

mylist = (3,55,4,6,33,8,12,14)

print(evenNumbers(mylist))