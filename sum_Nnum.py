def sum_Nnum(num):
    s=0
    for i in range(num+1):
        s+=i
    return s
num=int(input("Enter the Number: "))
print(sum_Nnum(num))    
