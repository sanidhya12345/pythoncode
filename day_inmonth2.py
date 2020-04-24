def number_days(m,mf,l1,l2):
    if m >= 1 and m <= 12:
        if m in l1:
            print(31)
            if m in l2:
                print(30)
        else:
            print(28)
    else:
        print("Wrong month value.")


month=int(input())
mfeb=28
lst1=[1,3,5,7,8,10,12]
lst2=[4,6,9,11]
number_days(month,mfeb,lst1,lst2)