# Q1:
def vowels_letters(text):
    if not text :
        return 0
    character = text[0].lower()
    vowels =['a','e','i','o','u']
    if character[0] in vowels:
        return 1 + vowels_letters(text[1:])
    else:
        return vowels_letters(text[1:])

user_input =input("Input the text : ")   
print(f'The vowels in this sentence({user_input})is: {vowels_letters(user_input)}')

# Q2:
numbers = [40,35,10,15,20]
mapped_number = map(lambda item : item * item ,numbers)
print(list(mapped_number))