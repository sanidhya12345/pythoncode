gifts=[25,64,9,4,100]
k=4
gifts.sort()
n=len(gifts)
for i in range(k):
    gifts[n-1]=int(gifts[n-1]**0.5)
    gifts.sort()
print(sum(gifts))