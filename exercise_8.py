# Write an algorithm that takes a list of strings and returns a new list containing 
# only the strings that start with a vowel (a, e, i, o, u).

def returnVowel(value):
    new_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in value:
        if word[0].lower() in vowels:   # Check if the first letter is in the list of vowels, I learned about 'in' here 
              new_list.append(word)
     
    return new_list


my_list = ['apple','banana','strawberry','elma','armut']
print(returnVowel(my_list))


