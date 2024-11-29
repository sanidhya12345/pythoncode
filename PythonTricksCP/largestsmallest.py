#python trick to find the n largest and n smallest of the list

import heapq

arr=[110, 25, 38, 49, 20, 95, 33, 87, 80, 90]

#3 largest element of the array

print(heapq.nlargest(3,arr))

#4 smallest elements of the array

print(heapq.nsmallest(4,arr))