# how to create a set

s={}
st=set()
print(s)
print(type(st))

#methods on sets

#1.add()

fruits={'apple','banana','cherry'}
fruits.add('orange') #aads an element to the set
print(fruits) #{'banana', 'orange', 'cherry', 'apple'}

#2.clear()

fruits={'apple','banana','cherry'}
fruits.clear()# removes all the elements from the set
print(fruits) # set()

#3.copy()

fruits={'apple','banana','cherry'}
a=fruits.copy() # returns a copy of the set
print(a) # {'banana', 'cherry', 'apple'}

#4.difference()

x={'a','b','c'}
y={'a','b','d'}
z=x.difference(y) # returns a set containing the difference between two sets
print(z) # {'c'}

#5.difference_update()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.difference_update(y) # removes the items from the first set those are also included in second set
print(x) # {'banana', 'cherry'}

#6.discard()

fruits={'apple','banana','cherry'}
fruits.discard('banana') # remove the specified items
print(fruits) # {'cherry', 'apple'}

#7.intersection()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
z=x.intersection(y) # returns the common element of the two sets
print(z) #{'apple'}

#8.intersection_update()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.intersection_update(y) # returns the items in this set that are not present in the other s[ecified set
print(x) #{'apple'}

#9.isdisjoint()

x={'apple','banana','cherry'}
y={'google','microsoft','facebook'}
z=x.isdisjoint(y) #returns whether two sets have a intersection or not
print(z)# True

#10.issubset()

x={'a','b','c'}
y={'f','e','c','d'}
z=x.issubset(y) # returns whether another set contains this set or not
print(z) # False

#11.issuperset()

x={'a','b','c','d','e','f'}
y={'a','b','c'}
z=x.issuperset(y) #returns whether this set contains another set or not
print(z) # True

#12.pop()

fruits={'apple','banana','cherry'}
fruits.pop()# removes an element from the set
print(fruits) # {'banana', 'cherry'}

#13.remove()

fruits={'apple','banana','cherry'}
fruits.remove('banana') # remove the particular element
print(fruits)# {'apple', 'cherry'}

#14.symmetric_difference()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
z=x.symmetric_difference(y)# returns a set with the symmetric differnce of the two sets
print(z)# {'microsoft', 'google', 'cherry', 'banana'}

#15.symmetric_difference_update()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.symmetric_difference_update(y)
print(x) # {'microsoft', 'google', 'cherry', 'banana'}

#16.union()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
z=x.union(y) # returns a set containing the union of sets
print(z) #{'apple', 'google', 'cherry', 'banana', 'microsoft'}

#17.update()

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.update(y) # update the set with the union of this set and others
print(x)# {'apple', 'google', 'cherry', 'banana', 'microsoft'}



