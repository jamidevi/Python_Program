def greatest_3num(a,b,c):
    if(a>b & a>c):
        return a
    elif(b>a & b>c):
        return b 
    else:
        return c 
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Thrid Number: "))
print(greatest_3num(a,b,c))