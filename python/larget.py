print("Enter the 3 numbers:")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if(a>b) and (a>c):
    print(a,"is largest")
elif(b>c) and(b>a):
    print(b,"is largest")
else:
    print(c,"is largest")
    

