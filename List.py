l=[1,2,3,4,6]
s=["sanidhya","uch bbu"]

'''
print(type(s)) type
'''

l=[[1,2,3],[3,4,5]]

#methods:--

#1.Indexing:---

print(l[1][1])
print(l[-1][-1])

#2.slicing:--

print(l[::-1])

#length of a list....

print(len(l))

#membership operators...

#1. in.

for i in range(0,len(l)):
    print(l[i])

for i in l:
    print(i)

#questions:-

#1.program to print elements of a list in a separate line positive or negative..

s=[1,2,3,4,5]
for i in range(0,len(s)):
    print("+ve index",i," ","-ve index",i-len(s)," ",s[i])

#comparing lists...

'''l1=[3,4,5]
l2=[2,4,5]
print(l1==l2)

print(l1[::-1])'''

'''l1=[1,2,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s1=l1 [5:15:2]
s2=l1 [::4]
sum=avg=0
print("Slice 1")
for a in s1:
   sum+=a
   print(a,end='')
print()
print("Slice 2")
sum=0
for a in s2:
    sum+=a
    print(a,end='')
print()
avg=sum/len(s2)
print("Average of the elements of s2",avg)'''

'''a=[1,3,5]
b=a.copy()
print(b)'''

l1=[1,2,3,4,5,6]
l2=l1.copy()
print("the original list",l1)
print("the created list",l2)
l1[0]+=10
l2[-1]+=10
print("the newly created list1",l1)
print("the newly created list2",l2)

a=[[1,3,4,],9,0]
print("length of a ",len(a))
a="vanshika"
print(list(a))
print(type(a))

a=[1,8,9]
b=a.index(8)
print(b)

friends=["vanshika","sneha"]
friends.append("garvita")
print(friends)

a=[1,3,5]
a.append(4)
print(a)

c=[45,78,89]
c.extend([89,98])
print(c)

'''c.insert(len(c),"vanshika")
print(c)
c.insert(-2,"vanshika")
print(c)'''

#Functions of tuple:=
'''
1.Empty tuple ---> T=tuple()
2.Single element tuple ----> t=(1)
3.Long tuples ----> sqrs=(0,1,4,9,16,25,
                         36,49,64,81,100)
4.Nested tuples ---->t1=(1,2,(3,4))
 #1. creating a tuple from existing sequences ---> t1=tuple('hello')
                                                 print(t1)  output= ('h','e','l','l','o')
 #2.t1=tuple(input("enter tuple elements:-))
    enter tuple elements:-098765
    ('0','9','8','7','6','5')
 #3.tuple=eval(input("enter tuple to be added:-))
    print(tuple)
    output:----> enter tuple to be added:-(8,9,[7,9],"jk")
    (8,9,[7,9],"jk")
5. length --> len(T)
6.Indexing and slicing ---> T[i] = returns the item at index
                            T[i:j]= returns i and j-1
                            T[i:j:n]= j ki index chodkar i aur j ki th term.
                            **--> tp1=(10,12,14,20,22,24,30,32,34)
                            tp1[0:10:2] output--> (10,14,20,30,34)
                            tp1[2:10:3] output--> (14,24,34)
                            tp1[::3] output--> (10,20,30) ---> (no start and no stop given only step is given)
7.Membership operators:- "in" gives true or present in tuple or "not in"
                          gives false or not present in tuple.
8.Concatenation and Replications ----> the concantenate (+) add tuple to the end of another 
                 and replicate(*) repeats a tuple.
$@! Accessing individual elements --> 
 vowels=('a','e','i','o','u')
 vowels[0]='a'
$@! Traversing a tuple ---> 
    T=('P','y','t','h','o','n')
    for a in T:
         print(T[a])
     output ---> P
                 y
                 t
                 h
                 o
                 n
9. del function ---> del(t1) --> delete the whole tuple t1
10 .max()
     max(t1)
11.min() 
    min(t1)
12.sum()
    val=(27,30,25,40)
    print(sum(val)) output--->122
13.index()
   t1=[3,4,5,6.0]
   t1.index(5) output--> 2
14.sorted()
  t1.sorted(_ 
15.t1.count()

'''