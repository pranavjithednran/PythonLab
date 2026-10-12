y1=int(input("enter starting year:"))
y2=int(input("enter ending year:"))

if(y1>y2):
    print("end year should be greater than the starting year")
else:
    print(f"leap year from {y1} and {y2}")
    for year in range(y1,y2+1):
        if(year%4==0 and year %100 !=0)or (year%400==0):
            print(year)
