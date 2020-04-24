# 1.
'''a Python function that accepts a string and calculate the number of uppercase letters and
lowercase letters.
Sample String: 'The quick Brow Fox'
Expected Output:
No. of Upper case characters: 3
No. of Lower case Characters: 12'''

#solution1:-

s=input()
c=0
a=0
for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
            c+=1
    if ord(i) >= 97 and ord(i) <= 122:
            a+=1
print("No. of upper case characters:",c)
print("No. of lower case characters:",a)

#2.Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List: [1,2,3,3,3,3,4,5]
#Unique List: [1, 2, 3, 4, 5]

#solution 2:-

#def remove_duplicate(lst):
lst=[1,2,3,3,3,3,4,5]
for i in lst:
    c=lst.count(i)
    if c>1:
     lst.remove(i)
print(lst)

#3.Write a Python program to reverse a string.
#Sample String: "1234abcd"
#Expected Output: "dcba4321"

def reverse(s):
    print(s[::-1])
str=input()
reverse(str)

#4.Write a Python to check whether a number is in a given range.

n=int(input())
if n in range(0,100):
        print("true")

#5.Write a Python program to print the even numbers from a given list.
#Sample List:[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result: [2, 4, 6, 8]

l=input().split(",")
p=[]
for i in l:
    if eval(i)%2==0:
        p.append(eval(i))
print(p)

#6.Write a Python program that accepts a hyphen separated sequence of words as input and/
# prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items: green-red-yellow-black-white
#Expected Result: black-green-red-white-yellow

l=input().split("-")
l.sort()
for i in l:
    print("-".join(l))
    break

#7.Write a Python program to create and print a list where the values are square of numbers between 1 and 30 (both included)

l=[1,2,3,4,5,6,7,8]
p=[]
for i in l:
    if 1<=(i**2)<=30:
       p.append(i**2)
print(p)

#8.
''' 
With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program
should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

n=int(input())
l1=[]
l2=[]
for i in range(1,n+1):
    l1.append(i)
    l2.append(i**2)
res={l1[i]:l2[i] for i in range(len(l1))}
print(res)

#9.
'''Write a program which accepts a sequence of comma-separated numbers from console and
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

l=input().split(",")
t=tuple(l)
print(l)
print(t)

#10.
'''Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

l=input().split("-")
l.sort()
for i in l:
   print("-".join(i))
   break

#11.
'''Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:again and hello makes perfect practice world'''

l=input().split(" ")
c=0
for i in l:
    l.count(i)
    if l.count(i)>1:
        l.remove(i)
l.sort()
print(" ".join(l))

#12.Write a program that accepts a sentence and calculate the number of letters and digits.
'''Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS - 10
DIGITS - 3'''

s=input()
let=0
dig=0
for i in s:
    if ord(i)>=95 and ord(i)<=122:
        let+=1
    if ord(i)>=65 and ord(i)<=90:
        let+=1
    if "0"<=i<="9":
        dig+=1
print("LETTERS - ",let)
print("DIGITS - ",dig)

#13.
'''Write a program to print odd number in a list. The list is input by a sequence of commaseparated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''

l=input().split(",")
for i in l:
    if eval(i)%2==0:
        l.remove(i)
print(",".join(l))

#14.Program to find the missing number in a given arithmetic progression list
l=[2,6,8,10,12,14,16]
p=[]
for i in range(1,len(l)+1):
        p.append(2*i)
for i in l:
    for j in p:
        if i not in j:
            print(i)

