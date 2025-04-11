class Solution:

    def sum_left(self,num,leng)-> int:
        sum=0
        for i in range(0,leng//2):
            sum+=int(num[i])
        return sum
    def sum_right(self,num,leng)-> int:
        sum=0;
        for i in range((leng//2),leng):
            sum+=int(num[i])
        return sum
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            s=str(i)
            leng=len(s)
            if leng%2==0:
                sl=self.sum_left(s,leng)
                sr=self.sum_right(s,leng)  
                if sr==sl:
                    count+=1
        return count

low=11
high=11
s=Solution()
print(s.countSymmetricIntegers(low,high))
