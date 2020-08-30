# alphabetical pattern:-
'''
$$$$$$$$
$      $
$      $
$$$$$$$$
$      $
$      $
$      $
'''
for i in range(1,8):
    if i==1 or i==4:
      print("$"*8)
    else:
      print("$"+" "*6+"$")
'''
$$$$$$$$
$      $
$      $
$$$$$$$$
$      $
$      $
$$$$$$$$      
'''

for i in range(1,8):
    if i==1 or i==4 or i==7:
        print("$"*8)
    else:
        print("$"+" "*6+"$")

'''
$$$$$$$$
$
$
$
$
$
$$$$$$$$
'''
for i in range(1,8):
    if i==1 or i==7:
        print("$"*8)
    else:
        print("$")
'''
$$$$$$$
$      $ 
$       $
$       $
$       $
$      $ 
$$$$$$$
'''
for i in range(1,8):
    if i==1 or i==7:
       print("$"*7)
    elif i==2 or i==6:
       print("$"+" "*6+"$")
    else:
       print("$"+" "*7+"$")
'''
$$$$$$$$
$
$
$$$$$$
$
$
$$$$$$$$
'''
for i in range(1,8):
    if i==1 or i==7:
        print("$"*8)
    elif i==4:
        print("$"*6)
    else:
        print("$")
'''
$$$$$$$$
$
$
$$$$$$$
$
$
$
'''
for i in range(1,8):
    if i==1:
        print("$"*8)
    elif i==4:
        print("$"*7)
    else:
        print("$")
'''
 $$$$$$
$
$
$   $$$
$     $
 $$$$$$
      $ 
'''
for i in range(1,8):
    if i==1 or i==6:
        print(" "+"$"*6)
    elif i==2 or i==3:
        print("$")
    elif i==4:
        print("$"+" "*3+"$$$")
    elif i==5:
        print("$"+" "*5+"$")
    else:
        print(" "*6+"$")

'''
$     $
$     $
$     $
$$$$$$$
$     $
$     $
$     $
'''

for i in range(1,8):
    if i==4:
        print("$"*7)
    else:
        print("$"+" "*5+"$")
'''
$$$$$$$
   $
   $
   $
   $
   $
$$$$$$$
'''

for i in range(1,8):
    if i==1 or i==7:
        print("$"*7)
    else:
        print(" "*3+"$"+" "*3)

'''
$$$$$$$
    $
    $
    $
    $
$   $
$$$$ 
'''

for i in range(1,8):
    if i==1:
        print("$"*7)
    elif i==7:
        print("$"*4)
    elif i==6:
        print("$"+" "*3+"$")
    else:
        print(" "*4+"$")

'''
$   $
$  $
$ $
$$
$ $
$  $
$   $

'''
g=4
h=1
for i in range(1,8):
    if i==4:
        print("$"*2)
    if i==1 or i==2 or i==3:
        print("$"+" "*g+"$")
        g=g-1
    if i==5 or i==6 or i==7:
        print("$"+" "*h+"$")
        h=h+1

'''
$
$
$
$
$
$
$$$$$$$
'''
for i in range(1,8):
    if i==7:
        print("$"*7)
    else:
        print("$")

'''
$     $
$$   $$
$ $ $ $ 
$  $  $
$     $
$     $
$     $
'''
for i in range(1,8):
    if i==1:
        print("$"+" "*5+"$")
    if i==2:
        print("$$"+" "*3+"$$")
    if i==3:
        print("$"+" "+"$"+" "+"$"+" "+"$")
    if i==4:
        print("$"+" "*2+"$"+" "*2+"$")
    else:
        print("$"+" "*5+"$")
'''
$     $
$$    $
$ $   $
$  $  $
$   $ $
$    $$
$     $
'''
g=0
h=4
for i in range(1,8):
    if i==1 or i==7:
        print("$"+" "*5+"$")
    else:
        print("$"+" "*g+"$"+" "*h+"$")
        h=h-1
        g=g+1

'''
$$$$$$$
$     $
$     $
$     $
$     $
$     $
$$$$$$$
'''

for i in range(1,8):
    if i==1 or i==7:
        print("$"*7)
    else:
        print("$"+" "*5+"$")

'''
$$$$$$$
$     $
$     $
$$$$$$$
$
$
$
'''
for i in range(1,8):
    if i==1 or i==4:
        print("$"*7)
    if i==2 or i==3:
        print("$"+" "*5+"$")
    if i==5 or i==6 or i==7:
        print("$")
'''
$$$$$$$
$     $
$     $
$     $
$  $  $
$$$$$$
       $  
      
'''
for i in range(1,8):
    if i==1:
        print("$"*7)
    if i==2 or i==3 or i==4:
        print("$"+" "*5+"$")
    if i==5:
        print("$"+" "*2+"$"+" "*2+"$")
    if i==6:
        print("$"*6)
    if i==7:
        print(" "*7+"$")
'''
$$$$$$$
$     $
$     $
$$$$$$$
$ $
$  $
$   $
'''
g=1
for i in range(1,8):
    if i==1 or i==4:
        print("$"*7)
    elif i==2 or i==3:
        print("$"+" "*5+"$")
    elif i==5 or i==6 or i==7:
        print("$"+" "*g+"$")
        g=g+1
'''
$$$$$$$
   $
   $
   $
   $
   $
   $
'''

for i in range(1,8):
    if i==1:
        print("$"*7)
    else:
        print(" "*3+"$")
'''
$      $
$      $
$      $
$      $
$      $
$      $
$$$$$$$$
'''
for i in range(1,8):
    if i==7:
        print("$"*8)
    else:
        print("$"+" "*6+"$")

'''
$           $
 $         $
  $       $
   $     $
    $   $
     $ $
      $
'''
h=0
g=11
for i in range(1,8):
    if i!=7:
     print(" "*h+"$"+" "*g+"$")
     h=h+1
     g=g-2
    else:
     print(" "*h+"$")

'''
$         $
$         $
$         $
$    $    $
$   $  $  $
$ $     $ $
$         $
'''
for i in range(1,8):
    if i==1 or i==2 or i==3 or i==7:
        print("$"+" "*9+"$")
    if i==4:
        print("$"+" "*4+"$"+" "*4+"$")
    if i==5:
        print("$"+" "*3+"$"+" "*2+"$"+" "*2+"$")
    if i==6:
        print("$ $"+" "*5+"$ $")

'''
$     $
 $   $
  $ $
   $
  $ $
 $   $
$     $
'''
h=0
g=5
k=2
l=1
for i in range(1,8):
    if i==4:
        print(" "*3+"$")
    if i==1 or i==2 or i==3:
        print(" "*h+"$"+" "*g+"$")
        g=g-2
        h=h+1
    if i==5 or i==6 or i==7:
        print(" "*k+"$"+" "*l+"$")
        k=k-1
        l=l+2
'''
$     $
 $   $
  $ $
   $
   $
   $
   $
'''

h=0
g=5
for i in range(1,8):
    if i==4:
        print(" "*3+"$")
    if i==1 or i==2 or i==3:
        print(" "*h+"$"+" "*g+"$")
        g=g-2
        h=h+1
    if i==5 or i==6 or i==7:
        print(" "*3+"$")
'''
$$$$$$$
     $
    $
   $
  $
 $
$$$$$$$     
'''
h=5
for i in range(1,8):
    if i==1 or i==7:
        print("$"*7)
    else:
        print(" "*h+"$")
        h=h-1