list1=[2,4,-6,-8,9,7]
list2=[i for i in list1 if(i>0)]
print (f"positve list={list2}")


list4=[1,2,3,4,5,6]
list3=[i**2 for  i in list4]
print(list3)


word=input("enter a string")
listvowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are {listvowel}")


w=input("enter any string: ")
ordinaval=[ord(i) for i in w]
print(ordinaval)
