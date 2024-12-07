def minimumSize( nums, maxOperations):
        low=1
        high=max(nums)
        while low<high:
            m=(low+high)//2
            cnt=sum((x-1)//m for x in nums)
            if cnt<=maxOperations: 
                high=m
            else: 
                low=m+1
        return high
nums=list(map(int,input().split( )))
maxops=int(input())
print(minimumSize(nums,maxops))