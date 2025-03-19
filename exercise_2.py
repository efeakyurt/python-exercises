#Write an algorithm that calculates the sum of all the numbers in a list


def sumList(values):
    # Step 1: Initialize a variable to hold the sum
    total_sum = 0
    
    # Step 2: Iterate through the list
    for number in values:
        # Step 3: Add each number to the sum
        total_sum += number
    
    # Step 4: Return the sum
    return total_sum


my_List = [1,99,3,7,20]
print(sumList(my_List))