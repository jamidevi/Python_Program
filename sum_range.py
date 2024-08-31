def sum_range(n):
    s=0
    for i in range(n):
        s+=i
    return s 
n=int(input("Enter the Number: "))
print(sum_range(n))    