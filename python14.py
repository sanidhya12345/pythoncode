l=list(input().split(" "))
count_number=0
count_string=0
for i in l:
    if i.isnumeric():
        count_number+=1
    else:
        count_string+=1
print("Numbers:-",count_number)
print("Strings",count_string)
