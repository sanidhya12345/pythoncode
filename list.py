# how to create a list

l=[]
lst=list() #using list constructor
print(l,type(l)) # [] <class 'list'>
print(lst,type(lst)) # [] <class 'list'>

# accessing the value of the list

#1.indexing

lst=[1,2,3,4,5,6]
p=lst[-3] #indexing
print(p) # 4

#2.slicing

lst=[1,2,3,4,5,6]
p=lst[0:3]
print(p)# [1, 2, 3]

# list is mutable
lst=[1,2,3,4,5,6]
lst[3]=8 # item assignment allowed (changeable at run time ) update item
print(lst)# [1, 2, 3, 8, 5, 6]

#list methods

#1.append()

lst=[1,2,3,4,5]
lst.append(4) # adds an element at the end of the list
print(lst) # [1, 2, 3, 4, 5, 4]

#2.clear()

lst=[1,2,3,4,5]
lst.clear() # removes all the elements of the list
print(lst)# []

#3.copy()

lst=[1,2,3,4,5]
p=lst.copy() # returns a copy of the list
print(p) # [1, 2, 3, 4, 5]

#4.count()

lst=[1,2,2,3,4,4,5]
p=lst.count(4) #return the number of elements with specified value
print(p) # 2

#5.index()

lst=[1,2,3,4,5]
p=lst.index(3) # return the index number of the particular element
print(p) #2

#6.insert()

lst=[1,2,3,3,4,5]
lst.insert(2,34) # inserts an element to the specified postion
print(lst) # [1, 2, 34, 3, 3, 4, 5]

#7.pop()

lst=[1,2,3,4,5,6]
lst.pop(2)# delete the particular element(by its specfied position) from the list
print(lst) # [1, 2, 4, 5, 6]

#8.remove()

lst=[1,2,3,4,5]
lst.remove(5) # remove the particular element by its specified value
print(lst) # [1, 2, 3, 4]

#9.reverse()

lst=[1,2,3,4,5,6]
lst.reverse()# reverse the order of the list
print(lst)# [6, 5, 4, 3, 2, 1]

#10.sort():- this sorts the list in their ascending order

lst=[100,245,34,45,55]
lst.sort() # sorts the list in ascending order
print(lst)# [34, 45, 55, 100, 245]

## sort the list with descending order.

lst=[1,2,3,56,54,67,89,334]
lst.sort(reverse=True)
print(lst) #[334, 89, 67, 56, 54, 3, 2, 1]

#11.extend()

lst=[1,2,3,4,5]
lst2=[6,7,8,9]
lst.extend(lst2)# adds the elements of the list,to the end of the current list
print(lst) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#basic list operations
#1.length of the list
lst=[1,2,3,4,5,6]
p=len(lst)
print(p) # 6

#2.cocatenation

lst1=[1,2,3,4,5]
lst2=[6,7,8,9]
lst3=lst2+lst1
print(lst3)# [6, 7, 8, 9, 1, 2, 3, 4, 5]

#3. repetation

lst=[4]
p=lst*4
print(p)# [4, 4, 4, 4]

#4.membership

lst=[1,2,3,4,56]
p=56 in lst
print(p)# True

#5.iteration

lst=[1,2,3,4,6]
for i in lst:
    print(i,end=" ")# 1 2 3 4 6

#6.find the maximum of the list

lst=[1,2,3,4,5,6]
p=max(lst)
print(p)# 6

#7.find the minimum of the list

lst=[1,2,3,4,5,6]
p=min(lst)
print(p)#1



