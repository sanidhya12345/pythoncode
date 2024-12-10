from collections import defaultdict
def totalfruits(arr):
    map={arr[i]:0 for i in range(len(arr))}
    i=0
    j=0
    n=len(arr)
    maxlen=0
    while j<n:
        map[arr[j]]+=1
        if len(map)>2:
            map[arr[i]]=-1
            if map[arr[i]]==0:
                del map[arr[i]]
            i+=1
        maxlen=max(maxlen,j-i+1)
        j+=1
    return maxlen
arr=[2,1,2]
print(totalfruits(arr))