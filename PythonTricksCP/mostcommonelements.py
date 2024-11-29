#trick to find the n most common elements

from collections import Counter

arr=[1,2,3,4,5,2,3,4,5,5]
counter=Counter(arr)
top_three=counter.most_common(3)
print(top_three)