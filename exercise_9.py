# Write an algorithm that takes a list of integers and returns a new list where each number is replaced by the 
# square of the number, but only if the number is positive. Negative numbers should be unchanged, 
# and zero should be excluded from the new list.

def createList(values):
    empty_list = []
    for number in values:
        if number > 0:
            number = number*number
            empty_list.append(number)
        elif number == 0:
            continue
        else:
            empty_list.append(number)

    return empty_list

my_list = [2,-4,12,-56,0,-1,16]
print(createList(my_list))
