first=int(input("enter the first side of the triangle:-"))
second=int(input("enter the second side of the triangle:-"))
third=int(input("enter the third side of the triangle:-"))
perimeter=(first+second+third)/2
area=(perimeter*(perimeter-first)*(perimeter-second)*(perimeter-third))**0.50
print("Area of triangle is:- ",area)