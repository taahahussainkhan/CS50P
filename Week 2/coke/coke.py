
str=input('Input: ')
vowels = ['a','e','i','o','u']

print('Ouput: ',end='')

for s in str:
    if s.casefold() not in vowels:
        print(s,end='')

print()