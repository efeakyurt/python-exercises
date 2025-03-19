# Write an algorithm that takes a list of strings and returns a new list containing 
# only the strings that start with a vowel (a, e, i, o, u).


def vowelList(values):

    newList = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in values:
        if word[0].lower() in vowels:   # Check if the first letter is in the list of vowels, I learned about 'in' here 
            newList.append(word)
    return newList

myList=["elma","armut","cilek","muz","orange"]
print(vowelList(myList))