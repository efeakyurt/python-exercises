# Write an algorithm that checks whether a given list of integers contains any duplicates

def checksame(values):
    seen = set()  # Initialize an empty set to track seen elements
    
    for number in values:
        if number in seen:  # Check if the number is already in the set
            print("There is a duplicate value:", number)
            return True
        else:
            seen.add(number)  # Add the number to the set
    
    print("No duplicate values found")
    return False