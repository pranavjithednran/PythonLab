def disp_pyrmid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print()
n=int(input("enter the number of steps: "))
if n<1:
    print("enter a positive number")
else:
    disp_pyrmid(n)
