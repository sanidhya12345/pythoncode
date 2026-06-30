adjacencyList=[[1,0,0],[1,0,1],[1,1,0]]

# directly we cannot use sum function as it is a list of list
# totalsum=sum(adjacencyList)

totalsum=sum(sum(adjacencyList,[]))
print(totalsum) # 5

simplelist=[[1,2,3],[4,5,6]]
singlelist=sum(simplelist,[])
print(singlelist) # 1 2 3 4 5 6