from typing import List
def sequentialDigits(low: int, high: int) -> List[int]:

    l=[]
    for _ in range(10):
        l.append([])
    
    digit=3
    for i in range(10):
        if i==2:
            l[2].append(12)
        elif i>2:
            num=l[i-1][0]*10+digit
            l[i].append(num)
            digit+=1
    
    for i in range(10):
        if i>=2:
            start=l[i][0]
            gap=int('1'*len(str(start)))
            num=start+gap

            while len(str(num))==i and str(num)[-1]!='0':
                l[i].append(num)
                num=num+gap
    sdl=len(str(low))
    edl=len(str(high))

    combined=[]
    for i in range(sdl,edl+1):
        combined+=l[i]
    
    result=[]
    for i in combined:
        if i>=low and i<=high:
            result.append(i)
    return result

print(sequentialDigits(12,30))




