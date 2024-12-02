def checkUnique(l):
    filtered = [x for x in l if x != '.'] 
    return len(set(filtered)) == len(filtered)


board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

crow=0
for i in range(0,9):
    row=[]
    for j in range(0,9):
        row.append(board[i][j])
    if checkUnique(row):
        crow+=1
ccol=0
for i in range(0,9):
    col=[]
    for j in range(0,9):
        col.append(board[j][i])
    if checkUnique(col):
        ccol+=1
        
cmat=0
ptr=0
for k in range(ptr,ptr+3):
    l=[]
    for i in range(k):
        for j in range(0,3):
            l.append(board[i][j])
    if checkUnique(l):
        cmat+=1
    l=[]
    for i in range(k):
        for j in range(3,6):
            l.append(board[i][j])
    if checkUnique(l):
        cmat+=1
    l=[]
    for i in range(k):
        for j in range(6,9):
            l.append(board[i][j])
    if checkUnique(l):
        cmat+=1
    ptr+=3
print(crow)
print(ccol)         
print(cmat)