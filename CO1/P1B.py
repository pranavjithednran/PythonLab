import datetime
current=datetime.date.today().year
final=int(input("enter the final year"))
if final<current:
    print("final year must be greater than or eqaul to the current year")
else:
    print(f"leap year from{current} to {final}")
    for year in range(current,final+1):
        if(year%4==0 and year %100!=0) or (year%400==0):
            print(year)
