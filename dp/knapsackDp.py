#reursive code only

def knapsack(weight,profit,W,n):
    
    #base condition
    
    if n==0 or W==0:
        return 0
    
    #we have two choices for each item available either we include in the knapsack or not.
    #among two choices we will take the maximum of both choices
    if weight[n-1]<=W:
        return max(profit[n-1]+knapsack(weight,profit,W-weight[n-1],n-1),knapsack(weight,profit,W,n-1))
    
    #if the weight of the current item is more than the knapsack capacity we have to exclude that particular item from the knapsack.
    
    return knapsack(weight,profit,W,n-1)
        

n=3
W=3
profit=[1,2,3]
weight=[4,5,1]
print(knapsack(weight,profit,W,n))
