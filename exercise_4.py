# Write an algorithm that counts how many even numbers are in a given list of integers.




def isEven(value):
    total = 0
    for number in value:
        if number % 2 == 0:
            total += 1
    
    return total


int_list = [1,2,3,4,5,6,8,12]
print(isEven(int_list))