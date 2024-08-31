def even_odd_num(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"
num=int(input("Enter the Number: "))
print(even_odd_num(num))    