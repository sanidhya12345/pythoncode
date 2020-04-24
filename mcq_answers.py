#q2
a={'a':1,'b':2,'c':3}
print(a['a','b'])
print(a.get('a','b'))

# answer=key error

#q3
'''fruit={}
def addone(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1

addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))'''

# answer is 3

#q4

arr={}
arr[1]=1
arr['1']=2
arr[1]+=1
sum=0
for k in arr:
    sum+=arr[k]
print(sum)

#answer is 4

#q5

my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4
sum=0
for k in my_dict:
    sum+=my_dict[k]


print(sum)


