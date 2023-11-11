letter=input('Enter a letter: ')
if letter in {'a','e','i','o','u'}:
    print(letter,'is a vowel')
elif letter=='y':
    print(letter,'sometimes is a consonant and sometimes is a vowel')
else:
    print(letter,'is a consonant')