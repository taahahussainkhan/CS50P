def main():
    camelCase = input('camelCase: ')
    conversion(camelCase)

def conversion(camelCase):
    snake_case=''
    for c in camelCase:
        if c.islower():
            print(c,end='')
            snake_case=c
        if c.isupper():
            print('_',c.lower(),end='',sep='')
    print('')
main()