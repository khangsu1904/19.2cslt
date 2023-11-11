L =  input('Enter a letter: ')

if L == 'a' or L == 'e' or L == 'i' or L == 'o' or L == 'u':
    print(L, 'is a vowel.')
elif L == 'y':
    print(L,'could be both a vowel and a consonant under certain linguistic circumstances.')
else:
    print('The letter',L,'is consonant.')