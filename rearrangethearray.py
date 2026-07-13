class Solution:
    def minOperations(self, b):
        # code here
        MOD=10**9+7
        n=len(b)
        visited=[False]*(n+1)

        # this dictionary will store the maximum power of prime factors

        max_prime_powers={}

        #Step1: find the cycle length of each element

        for i in range(1,n+1):
            if not visited[i]:
                curr=i
                length=0

                # run a loop till the cycle comes at the starting point
                while not visited[curr]:

                    visited[curr]=True
                    
                    curr=b[curr-1]
                    length+=1
        
            #step2 and 3: Prime Factorization the cycle length and update the max_prime_powers

            temp=length
            d=2

            while d * d <= temp:
                if temp%d==0:
                    count=0
                    while temp%d==0:
                        count+=1
                        temp//=d

                    
                    if d in max_prime_powers:
                        max_prime_powers[d]=max(max_prime_powers[d],count)
                    else:
                        max_prime_powers[d]=count
                d+=1

            #if there is any prime number left.
            if temp>1:
                if temp in max_prime_powers:
                    max_prime_powers[temp]=max(max_prime_powers[temp],1)
                else:
                    max_prime_powers[temp]=1
            
        ans=1
        for prime, power in max_prime_powers.items():
            ans=(ans * pow(prime,power,MOD))%MOD

        return ans



        pass



b=[1,2,3]        
print(Solution.minOperations("",b))