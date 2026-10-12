square_area=lambda a:a**2
rectangle_area=lambda l,b:l*b
triangle_area=lambda ba,h: 0.5 *ba*h

a=int(input("enter the lenght:"))
print("area of the square:",square_area(a))

l=int(input("nter the breadth:"))
b=int(input("enter the breadth:"))
print("area of the triangle:",rectangle_area(l,b))

ba=int(input("enter the base:"))
h=int(input("emter the height:"))
print("area of the rectangle:",triangle_area(ba,h))
