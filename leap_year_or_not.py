def leapyear(a):
    if 1900<=a<=2019:
        if a%4==0 and a%400==0:
            if a%100==0:
                print("true")
        else:
                print("false")
year=int(input())
leapyear(year)
