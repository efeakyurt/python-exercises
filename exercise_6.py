# Write an algorithm that takes a list of integers and returns a 
# new list containing only the positive numbers from the original list.


def createList(values):
    positive_numbers = [] # initially we have defined an empty list 
    for number in values:
        if number > 0:
            positive_numbers.append(number)

    return positive_numbers
            

listel = [-1,2,-55,34,-345,7,-8]
print(createList(listel))

