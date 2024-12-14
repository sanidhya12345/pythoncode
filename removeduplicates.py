def removeDuplicates(arr,n):
    
    count=0
    for i in range(0,n-1):
        if arr[i]==arr[i+1]:
            count+=1
    return n-count   
    
arr=[1,2,2,2,3]
n=len(arr)
print(removeDuplicates(arr,n))