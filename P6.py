list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
if len(list1)==len(list2):
    print("the lists have same lenght")
else:
    print("the lists does not have same lenght");
print(f"b.sum of list1:{sum(list1)} and sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print("sum is same")
else:
    print("sum is not same")
common=set(list1) & set(list2)
if common:
    print(f"common values:{common}")
else:
    print("no common values")
    
