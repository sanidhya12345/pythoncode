# dictionary creation empty
d = {}
print(d, type(d)) # {} <class 'dict'>
d = dict() # dict constructor
print(d, type(d)) # {} <class 'dict'>


# dictionary operation
dct = { 'rolln':30, 'cpi':8.0, 'section':'A', 'name':'akshay'}
print(dct, type(dct))

# accessing the element
d = dct['name'] # element at given key
print(d) # 'akshay'

# keys() : get all the keys of dict
dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
out1 = dct.keys()
print(out1) # dict_keys(['name', 'rolln', 'cpi', 'section'])

out2 = dct.values()
print(out2, type(out2)) # dict_values(['Govind', 30, 7.0, 'E']) <class 'dict_values'>

#methods of dictionary

#1.update

dct={'name':'sanidhya','section':'O','rolln':22}
dct['Name']='mayank'
print(dct)  # {'rolln': 22, 'Name': 'mayank', 'section': 'O', 'name': 'sanidhya'}

#2.delete

dct={'name':'sanidhya','section':'O','rolln':22}
del dct['name'] # remove entry with key name
print(dct) # {'rolln': 22, 'section': 'O'}

#3.pop()

dct={'name':'sanidhya','section':'O','rolln':22}
d=dct.pop('name') # remove the key from dictionary and return the key value
print(d) # sanidhya

#4.clear()

dct={'name':'sanidhya','section':'O','rolln':22}
dct.clear() # remove all the entries of dictionary
print(dct) # {}

#5.copy()

dct={'name':'sanidhya','section':'O','rolln':22}
d=dct.copy() # return shallow copy of dictionary
print(d) # {'name':'sanidhya','section':'O','rolln':22}

#6.get()

dct={'name':'sanidhya','section':'O','rolln':22}
d=dct.get('rolln') # return the value of the key
print(d) # 22

#7.fromkeys()

dct={'name':'sanidhya','section':'O','rolln':22}
d=dct.fromkeys(['a','b','c','d'],0) # creates dictinary from given sequence
print(d) # {'a': 0, 'd': 0, 'b': 0, 'c': 0}

#8.items

dct={'name':'sanidhya','section':'O','rolln':22}
d=dct.items() # returns the view of the dictionary (keys,values)
print(d)# dict_items([('rolln', 22), ('section', 'O'), ('name', 'sanidhya')])

#9.popitem()

dct={'name':'sanidhya','section':'O','rolln':22}
dct.popitem() # returns and removes element from dictionary
print(dct) # {'section': 'O', 'name': 'sanidhya'}

#10.setdefault()

D1 = {'Name': 'Sachin', 'Section': 'O', 'Address': 'IIT Delhi', 'Rolln':20}
D1.setdefault('Rolln', 'NA') # inserts a key with a value if key is not present
print(D1) # {'Name': 'Sachin', 'Section': 'O', 'Address': 'IIT Delhi', 'Rolln': 20}








