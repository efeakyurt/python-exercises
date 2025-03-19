#Write an algorithm that calculates the sum of all the numbers in a list



def calculateSum(values):
    total_sum = 0

    for number in values:
        total_sum += number

    return total_sum


numberlist = (3,5,4,78,2)
print(calculateSum(numberlist))