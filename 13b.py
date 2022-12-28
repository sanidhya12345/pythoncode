dct={"k1":"v1","k2":"v2","k3":"v3"}
print("Original Dictionary",dct)
dct_rev=dict([(value,key) for key,value in dct.items()])
print("After Swapping",dct_rev)