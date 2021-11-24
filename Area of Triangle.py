# s = (a+b+c)/2
# Area = ( s(s-a)*(s-b)*(s-c) ) ** 0.5

a = input ( "Enter the sides of a triangle (in cm) :" )
b = input ("Next side :" )
c = input ("Last one :" )

sum = float(a) + float(b) + float(c)
s = sum/ 2

Area = ( s*(s-float(a))*(s-float(b))*(s-float(c) )) ** 0.5
Area_last = f"The Area of the triangle with the given sides is {Area} sq.cm "
print(Area_last)



