def checkTwoAdjacent(arr,i,j):
    return abs(arr[i]-arr[j])<=1


def leetcode1846(arr):
    arr.sort()
    if arr[0]!=1:
        arr[0]=1
    if len(arr)==1:
        return max(arr[0])
    for i in range(0,len(arr)-1):
        if not checkTwoAdjacent(arr,i,i+1):
            arr[i+1]=arr[i]+1
    return max(arr)

arr=[1,6,6]
print(leetcode1846(arr))