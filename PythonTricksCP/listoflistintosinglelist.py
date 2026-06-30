import itertools

lst=[[1,2],[3,4],[4,5]]
singlelist=list(itertools.chain.from_iterable(lst))
print(singlelist)