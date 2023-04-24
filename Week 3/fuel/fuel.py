
def main():
    fraction = get_fuel()
    print(fraction)
def get_fuel():
        while True:
            try:
                fraction = input('Fraction: ')
                x, y = fraction.split('/')
                x = int(x)
                y = int(y)
                if  0 <= x/y <= 0.1:
                    return('E')
                elif 0.9 <= x/y <= 1:
                    return('F')
                elif 0.1 < x/y < 0.9:
                    return str(round(x / y * 100)) + "%"
            except (ValueError, ZeroDivisionError):
                    pass

main()