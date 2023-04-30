months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        date = input('Date: ')
        try:
            month,day,year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if (int (month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                print (f'{year}-{month:02}-{day:02}')
                break
        except:
            try:
                if "," in date:
                    month,day,year = date.split(' ')
                    day = day.replace(',','')
                    day = int(day)
                    year = int(year)
                    if month in months and (int(day) >= 1 and int(day) <= 31):
                        month= (months.index (mnth)+1)
                        print (f'{year}-{month:02}-{day:02}')
                        break
            except:
                pass
main()