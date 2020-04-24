d={'x':1,'t':3,'d':4,'g':5}
z=list(d.keys())
c=list(d.values())
z.sort()
res={z[i]:c[i] for i in range(len(z))}
print(res)