def main():
    time=input('What time is it? ')
    converted_time=convert(time)
    if converted_time >= 7.00 and converted_time <= 8.00:
        print('breakfast time')                
    elif converted_time >= 12.00 and converted_time <= 13.00:
        print('lunch time')
    elif converted_time >= 18.00 and converted_time <= 19.00:
        print('dinner time')

def convert(time):
    x, y = time.split(":")
    hour = float(x)
    min = float(y) * 1 / 60
    return float(hour+min)

if __name__ == "__main__":
    main()
