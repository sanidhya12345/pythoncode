def smallestnumber(arr):

    current_x=0

    for i in range(len(arr)-1,-1,-1):
        current_x=(current_x + arr[i]+1)//2
    
    return current_x

print(smallestnumber([3,4,3,2,4]))