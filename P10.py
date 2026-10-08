n1=int(input("1:"))
n2=int(input("2:"))
n3=int(input("3:"))
if n1>n2 and n1>n3:
    print("the largest is",n1)
elif n2>n1 and n2>n3:
    print("the largest is",n2)
else:
    print("the largest is",n3)
