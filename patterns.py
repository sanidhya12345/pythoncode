#1.
'''
*****
*****
*****
*****
*****
'''
#solution=
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()

#2.
'''
11111
22222
33333
44444
55555
'''
#solution=
for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()

#3.
'''
12345
12345
12345
12345
12345
'''
#solution=
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()

#4.
'''
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
'''
for i in range(65,70):
    for j in range(1,6):
        print(chr(i),end="")
    print()
#5.
'''
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
'''
for i in range(1,6):
    for j in range(65,70):
        print(chr(j),end="")
    print()
#6.
'''
55555
44444
33333
22222
11111
'''
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end="")
    print()
#7.
'''
54321
54321
54321
54321
54321
'''
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end="")
    print()
#8.
'''
EEEEE
DDDDD
CCCCC
BBBBB
AAAAA
'''
for i in range(69,64,-1):
    for j in range(5,0,-1):
        print(chr(i),end="")
    print()
#9.
'''
EDCBA
EDCBA
EDCBA
EDCBA
EDCBA
'''
for i in range(5,0,-1):
    for j in range(69,64,-1):
        print(chr(j),end="")
    print()

#10.
'''
*
**
***
****
*****
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
#11.
'''
1
22
333
4444
55555
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
#12.
'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
#13.
'''
A
BB
CCC
DDDD
EEEEE
'''
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()
#14.
'''
A
AB
ABC
ABCD
ABCDE
'''
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()
#15.
'''
*****
****
***
**
*
'''
for i in range(1,6):
    for j in range(i,6):
        print("*",end="")
    print()
#16.
'''
11111
2222
333
44
5
'''
for i in range(1,6):
    for j in range(i,6):
        print(i,end="")
    print()
#17.
'''
12345
1234
123
12
1
'''
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()
#18.
'''
55555
4444
333
22
1
'''
for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end="")
    print()
#19.
'''
54321
5432
543
54
5
'''
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()
#20.
'''
EEEEE
DDDD
CCC
BB
A
'''
for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(i+64),end="")
    print()
#21.
'''
EDCBA
EDCB
EDC
ED
E
'''
for i in range(0,5):
    for j in range(4,i-1,-1):
        print(chr(j+65),end="")
    print()
#22.
''' 
    *
   **
  ***
 ****
*****   
'''
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print()
#23.
'''
    1
   22
  333
 4444
55555  
'''
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print(i,end="")
    print()
#24.
'''
*****
 ****
  ***
   **
    *
'''
for i in range(5,0,-1):
    for j in range(i,5):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print()