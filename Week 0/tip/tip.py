def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    num=d.replace('$','')
    num=float(num)
    return num


def percent_to_float(p):
    # TODO
    pnum=p.replace('%','')
    pnum=float(pnum)
    pnum=pnum/100
    return pnum

main()
