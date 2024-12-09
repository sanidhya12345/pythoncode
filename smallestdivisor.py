from math import ceil
def binaryHelper(nums,threshold):
    low=1
    high=max(nums)
    ans=0
    while low<=high:
        mid=(low+high)//2
        t=0
        for i in range(0,len(nums)):
            t+=ceil(nums[i]/mid)
        if t>threshold:
            low=mid+1
        else:
            high=mid-1
    return low
            
nums=[1,2,5,9]
threshold=6
print(binaryHelper(nums,threshold))
