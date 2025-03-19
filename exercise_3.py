# Write an algorithm that checks whether a given list of integers contains any duplicates



def ifSame(values):
    seen = set()  # Use a set to track seen elements
    for value in values:
        if value in seen:  # If the value is already in the set, it's a duplicate
            return True
        seen.add(value)  # Add the value to the set
    return False  # If no duplicates are found, return False



exp_list = [34,2,5,6,1,7,3,3]
print(ifSame(exp_list))
