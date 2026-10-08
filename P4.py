n=int(input("toal number of integars:"))
list1=[]
for i in range(n):
    a=int(input("enter an integar:"))
    if a<100:
        list1.append(a)
    else:
        list1.append("over")
print(list1)
