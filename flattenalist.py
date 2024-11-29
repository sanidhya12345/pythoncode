#how to flatten the list in python

import itertools
l=[[1,2,3],[4,5,6],[7,8,9]]

b=list(itertools.chain.from_iterable(l))

print(b)


#output: [1,2,3,4,5,6,7,8,9]