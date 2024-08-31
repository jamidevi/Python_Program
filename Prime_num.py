def prime_num(num):
    if(num<=1):
        return False
    elif(num==2):
        return True
    elif(num%2==0):
        return False 
    else:
        for i in range(3,int(num**0.5)+1,2):
            if(num%i==0):
                return False 
        
        return True
            
num=int(input("Enter the Number: "))
if(prime_num(num)):
    print(f"{num} is the Prime Number.")
else:
    print(f"{num} is the not Prime Number.")    