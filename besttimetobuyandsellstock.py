prices = [7,1,5,3,6,4]
m=prices[0]
max_profit=0

for i in range(1,len(prices)):
    m=min(m,prices[i])
    max_profit=max(max_profit,prices[i]-m)
print(max_profit)
