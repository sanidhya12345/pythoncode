n=int(input("Enter the number of users:-"))
l_name=[]
l_salary=[]
l_net=[]
for i in range(0,n):
    name=input("Enter user name:-")
    ba=int(input())
    hr=int(input())
    ta=int(input())
    sum=ba+hr+ta
    l_name.append(name)
    l_salary.append([ba,hr,ta])
    l_net.append(sum)
dct={l_name[i]:l_salary[i] for i in range(0,len(l_name))}
dct_net_salary={l_name[i]:l_net[i] for i in range(0,len(dct))}
print("Name ","Net Salary ")
for i in dct:
    print(i,dct_net_salary.get(i))
