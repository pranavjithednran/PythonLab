def find_fact(number):
    fact=[]
    for i in range(1,number+1):
       if number%i==0:
           fact.append(i)
    return fact
num=int(input("enter the number of row:"))
result=find_fact(num)
print(f"the factors of {num} are: {result}")
