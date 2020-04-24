def adjacent(str,lst):
    if len(str) % 2 != 0:
        print("Odd length.")
    else:
        for i in str:
            lst.append(i)
        for i in range(0, len(lst), 2):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print("".join(lst))

s=input()
l=[]
adjacent(s,l)