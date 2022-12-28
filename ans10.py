dct={"Ashish":90,"Anjali":85,"Neha":75,"Surbhi":50}
print("Original Dictonary",dct)
name=input("Enter the name you want to delete:-")
if name in dct:
    del dct[name]
print("Dictionary After deletion",dct)
